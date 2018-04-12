from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
import requests
import json
import os
import random
from faker import Faker

fake = Faker()
app = Flask(__name__)

dogs_db = [
	{'id' : '1', 'breed' : 'French bulldog', 'name' : 'Doggo', 'temporary guardian ID' : 'NONE', 'visits' : []},
	{'id' : '2', 'breed' : 'Chow Chow', 'name' : 'Sir Pup', 'temporary guardian ID' : 'NONE', 'visits' : []},
	{'id' : '3', 'breed' : 'Spaniel', 'name' : 'Coco', 'temporary guardian ID' : 'NONE', 'visits' : []},
	{'id' : '4', 'breed' : 'French bulldog', 'name' : 'Olive', 'temporary guardian ID' : '49612033268', 'visits' : []},
	{'id' : '5', 'breed' : 'German Shepherd', 'name' : 'Rex', 'temporary guardian ID' : '49608052145', 'visits' : []}
]

@app.route('/')
def hello():
	return'Welcome to the puppy shelter'

# GET information about all dogs from database as JSON
@app.route('/dogs', methods=['GET'])
def get_all_dogs():
	return jsonify(dogs_db)

# GET any dog by any parameter
@app.route('/dogs/<parameter>', methods=['GET'])
def get_dog(parameter):
	my_dog = [ dog for dog in dogs_db if (dog['id'] == parameter or 
		dog['breed'] == parameter or dog['name'] == parameter or
		dog['temporary guardian ID'] == parameter)]
	if len(my_dog) == 0:
		abort(404)
	return jsonify(my_dog[0])



# DELETE a dog from a database by ID (adopt)
@app.route('/dogs/<dog_id>', methods=['DELETE'])
def adopt_dog(dog_id):
	adopted_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id )]
	if len(adopted_dog) == 0:
		abort(404)
	dogs_db.remove(adopted_dog[0])
	return jsonify(adopted_dog[0]), 200

# POST a dog to a database (give away)
# Name is in url, id and breed have to be provided as JSON
@app.route('/dogs', methods=['POST'])
def give_away_dog():
	current_id = int(dogs_db[len(dogs_db) - 1]['id']) + 1
	new_dog = {
	'id' : str(current_id),
	'breed' : request.json['breed'],
	'temporary guardian ID' : request.json['temporary guardian ID'],
	'name' : request.json['name']
	}
	dogs_db.append(new_dog)
	
	return jsonify(new_dog), 201
	

# PUT change a dog
# Any parameter in URL
@app.route('/dogs/<dog_id>', methods = ['PUT'])
def change_dog(dog_id):
	changed_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id )]
	if len(changed_dog) == 0:
		abort(404)
	if 'name' in request.json:
		changed_dog[0]['name'] = request.json['name']
	if 'breed' in request.json:
		changed_dog[0]['breed'] = request.json['breed']
	if 'temporary guardian ID' in request.json:
		changed_dog[0]['temporary guardian ID'] = request.json['temporary guardian ID']

	return jsonify(changed_dog[0])

@app.route('/visits', methods=['GET'])
def get_all_visits():
	r = requests.get('http://172.18.0.1:81/visits/schedules')
	return r.text

# Get visits that belong to the dog by its guardian
@app.route('/dogs/<dog_id>/visits', methods = ['GET'])
def create_visit(dog_id):
	current_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id )]
	if len(current_dog) == 0:
		abort(404)
	url = 'http://172.18.0.1:81/visits/schedules'
	r = requests.get('{}/{}'.format(url, current_dog[0]['temporary guardian ID']))
	if r.status_code==200:
		current_dog[0]['visits'].append(r.json())
		return jsonify(current_dog[0])
	return r.text, 404

# Create a new visit
@app.route('/dogs/<dog_id>/visits', methods = ['POST'])
def add_visit(dog_id):
	current_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id )]
	if len(current_dog) == 0:
		abort(404)
	url = 'http://172.18.0.1:81/visits/schedules'
	header = {'content-type' : 'application/json'}
	new_visit = {
		'AK' : current_dog[0]['temporary guardian ID'],
		'Name' : current_dog[0]['name'],
		'Surname' : current_dog[0]['breed'],
		'Date' : str(fake.date_between(start_date='today', end_date='+1y')),
		'Time' : '{}:15'.format(random.randrange(8,20))
	}
	r = requests.post(url, json=new_visit)
	current_dog[0]['visits'].append(r.json())
	return jsonify(current_dog[0]), 201

# Delete a visit
@app.route('/dogs/<dog_id>/visits/<visit_id>', methods = ['DELETE'])
def delete_visit(dog_id, visit_id):
	current_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id )]
	# if len(current_dog) == 0 or len(current_dog[0]['visits']):
	if len(current_dog) == 0:
		abort(404)
	url = 'http://172.18.0.1:81/visits/schedules'
	for index in range(len(current_dog[0]['visits'])):
		if current_dog[0]['visits'][index]['ID'] == visit_id:
			r = requests.delete('{}/{}'.format(url, visit_id))
			current_dog[0]['visits'].remove(current_dog[0]['visits'][index])
			return jsonify(True), 200
	return jsonify(False), 404




if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', threaded=True)

