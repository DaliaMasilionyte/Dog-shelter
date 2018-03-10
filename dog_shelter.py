from flask import Flask
from redis import Redis
import os

dog_shelter = Flask(__name__)
redis = Redis(host='redis', port=6379)

dogs_dict = {
	'1' : {'id' : '1', 'breed' : 'French bulldog', 'name' : 'Doggo'},
	'2' : {'id' : '2', 'breed' : 'Chow Chow', 'name' : 'Sir Pup'},
	'3' : {'id' : '3', 'breed' : 'Spaniel', 'name' : 'Coco'},
	'4' : {'id' : '4', 'breed' : 'French bulldog', 'name' : 'Olive'},
	'5' : {'id' : '5', 'breed' : 'German Shepherd', 'name' : 'Rex'}
}


@app.route('/')
def hello():
	return'Welcome to the puppy shelter'

@app.route('/list_dogs')
def list_dogs():
	for key in dogs_dict:
		dogs_string += dog[key]['breed'] + dog[key]['name']
		dogs_string += '\n'
	return'These are our pupps:\n{}'.format(dogs_string)


@app.route('/adopt')
def adopt():
	return'You adopted a pup! There will be more sunshine!'

@app.route('/give_away')
def give_away():

	return'That was very cruel! Shame on you.'

if __name__ == "__main__":
	dog_shelter.run(host="0.0.0.0", debug=True)