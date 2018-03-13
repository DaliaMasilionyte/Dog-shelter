from flask import Flask
from flask import request
from flask import jsonify

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
	return jsonify({'Our Pupps':dogs_db})

# DELETE a dog from a database by ID (adopt)
@app.route('/dogs/<dog_id>', methods=['DELETE'])
def adopt_dog(dog_id):
	adopted_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id)]
	if len(adopted_dog) == 0:
		abort(404)
	dogs_db.remove(adopted_dog[0])
	return jsonify({'Your adopted pup:':adopted_dog[0]})

# POST a dog to a database (give away)
# Name is in url, id and breed have to be provided as JSON
@app.route('/dogs/<give_away_dog_name>', methods=['POST'])
def give_away_dog(give_away_dog_name):
	new_dog = {
	'id' : request.json['id'],
	'breed' : request.json['breed'],
	'temporary guardian' : 'NONE',
	'name' : give_away_dog_name
	}
	dogs_db.append(new_dog)
	return jsonify({'That was very cruel':new_dog})

# PUT (become) a dog guardian
# ID in URL, guardian name - provided as JSON
@app.route('/dogs/<dog_id>', methods = ['PUT'])
def become_guardian(dog_id):
	guarded_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id)]
	guarded_dog[0]['temporary guardian'] = request.json['temporary guardian']
	return jsonify({'You became a guardian': guarded_dog[0]})


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

