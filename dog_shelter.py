from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

import os

app = Flask(__name__)

dogs_db = [
	{'id' : '1', 'breed' : 'French bulldog', 'name' : 'Doggo', 'temporary guardian' : 'NONE'},
	{'id' : '2', 'breed' : 'Chow Chow', 'name' : 'Sir Pup', 'temporary guardian' : 'NONE'},
	{'id' : '3', 'breed' : 'Spaniel', 'name' : 'Coco', 'temporary guardian' : 'NONE'},
	{'id' : '4', 'breed' : 'French bulldog', 'name' : 'Olive', 'temporary guardian' : 'NONE'},
	{'id' : '5', 'breed' : 'German Shepherd', 'name' : 'Rex', 'temporary guardian' : 'NONE'}
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
		dog['temporary guardian'] == parameter)]
	if len(my_dog) == 0:
		abort(404)
	return jsonify(my_dog[0])




# DELETE a dog from a database by ID (adopt)
@app.route('/dogs/<parameter>', methods=['DELETE'])
def adopt_dog(parameter):
	adopted_dog = [ dog for dog in dogs_db if (dog['id'] == parameter or 
		dog['breed'] == parameter or dog['name'] == parameter or
		dog['temporary guardian'] == parameter)]
	if len(adopted_dog) == 0:
		abort(404)
	dogs_db.remove(adopted_dog[0])
	return jsonify(adopted_dog[0])

# POST a dog to a database (give away)
# Name is in url, id and breed have to be provided as JSON
@app.route('/dogs', methods=['POST'])
def give_away_dog():
	new_dog = {
	'id' : request.json['id'],
	'breed' : request.json['breed'],
	'temporary guardian' : request.json['temporary guardian'],
	'name' : request.json['name']
	}
	dogs_db.append(new_dog)

	response = jsonify(new_dog)
    response.status_code = 201
    response.headers['location'] = '/dogs/{}'.format(request.json['id'])
    response.autocorrect_location_header = False
    return response
	

# @app.route('/dogs/<parameter>', methods=['POST'])
# def add_to_dog():
# 	changed_dog = [ dog for dog in dogs_db if (dog['id'] == parameter || 
# 		dog['breed'] == parameter || dog['name'] == parameter ||
# 		dog['temporary guardian'] == parameter)]
	

# 	return jsonify({'dog':changed_dog})


# PUT change a dog
# Any parameter in URL
@app.route('/dogs/<parameter>', methods = ['PUT'])
def change_dog(parameter):
	changed_dog = [ dog for dog in dogs_db if (dog['id'] == parameter or 
		dog['breed'] == parameter or dog['name'] == parameter or
		dog['temporary guardian'] == parameter)]
	if len(changed_dog) == 0:
		abort(404)
	if 'id' in request.json:
		changed_dog[0]['id'] = request.json['id']
	if 'name' in request.json:
		changed_dog[0]['name'] = request.json['name']
	if 'breed' in request.json:
		changed_dog[0]['bred'] = request.json['breed']
	if 'temporary guardian' in request.json:
		changed_dog[0]['temporary guardian'] = request.json['temporary guardian']

	return jsonify(changed_dog[0])


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

