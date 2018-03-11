from flask import Flask
from flask import request
from flask import jsonify

import os

app = Flask(__name__)


dogs_db = [
	{'id' : '1', 'breed' : 'French bulldog', 'name' : 'Doggo'},
	{'id' : '2', 'breed' : 'Chow Chow', 'name' : 'Sir Pup'},
	{'id' : '3', 'breed' : 'Spaniel', 'name' : 'Coco'},
	{'id' : '4', 'breed' : 'French bulldog', 'name' : 'Olive'},
	{'id' : '5', 'breed' : 'German Shepherd', 'name' : 'Rex'}
]


@app.route('/')
def hello():
	return'Welcome to the puppy shelter'


@app.route('/dogs', methods=['GET'])
def get_all_dogs():
	return jsonify({'Our Pupps':dogs_db})


@app.route('/dogs/<dog_id>', methods=['DELETE'])
def adopt_dog(dog_id):
	adopted_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id)]
	if len(adopted_dog) == 0:
		abort(404)
	dogs_db.remove(adopted_dog[0])
	return jsonify({'Your adopted pup:':adopted_dog[0]})


@app.route('/dogs/<give_away_dog_name>', methods=['POST'])
def give_away_dog(give_away_dog_name):
	new_dog = {
	'id' : request.json['id'],
	'breed' : request.json['breed'],
	'name' : give_away_dog_name
	}
	dogs_db.append(new_dog)
	return jsonify({'That was very cruel':new_dog})


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

