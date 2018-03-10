from flask import Flask
from flask import request
from redis import Redis

import os

dog_shelter = Flask(__name__)
redis = Redis(host='redis', port=6379)

dogs_dict = {}
dog_id_list = []

with open('shelter.txt', 'r') as input_file:
    content = input_file.readlines()
    for line in content:

        dog_data = line.split()
        dogs_dict[dog_data[0]] = {'id' : dog_data[0], 'breed' : dog_data[1],
                                  'name' : dog_data[2]}


def delete_from_file(id):
    with open('shelter.txt', 'w') as output_file:
        new_shelter_list = ''
        for dog_id in dogs_dict:
            if dog_id != id:

                new_shelter_list += dogs_dict[dog_id]['id'] + ' ' + \
                                    dogs_dict[dog_id]['breed'] + ' ' + \
                                    dogs_dict[dog_id]['name'] + '\n'
        output_file.write(new_shelter_list)

def write_to_file(new_doggo):
    with open('shelter.txt', 'a') as output_file:
        output_file.write(new_doggo)



@app.route('/')
def hello():
	return'Welcome to the puppy shelter'

@app.route('/list_dogs')
def list_dogs():
	dogs_string = ''
	for key in dogs_dict:
		dogs_string += dogs_dict[key]['breed'] + ' named ' +  dogs_dict[key]['name']
		dogs_string += '\n'
	return'These are our pupps:\n{}'.format(dogs_string)


@app.route('/adoption')
def adoption():
	dog_ID = request.args.get('dog_ID', default = None, type = 'str')
	dog_ID = id
    if dog_ID in dogs_dict:
        adoption_protocol = "You adopted a pup! It's breed is {} and it's name is {}.\n" \
                            "There will be more sunshine!".format(dogs_dict[id]['breed'],
                                                                  dogs_dict[id]['name'])
        del dogs_dict[dog_ID]
        delete_from_file(dog_ID)
    else:
        adoption_protocol = "There is no such pup in the shelter. Look at our other cuties"

    return adoption_protocol

@app.route('/giveaway_dogs')
def give_away_dogs():
	current_ID = int(dog_id_list[-1])
    new_ID = current_ID + 1
    breed = request.args.get('breed')
    name = request.args.get ('name')

    new_doggo = str(new_ID) + ' ' + breed + ' ' + name
    
    write_to_file('\n{}'.format(new_doggo))
	return'That was very cruel! Shame on you.'

if __name__ == "__main__":
	dog_shelter.run(host="0.0.0.0", debug=True)