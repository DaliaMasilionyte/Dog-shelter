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



# with open('shelter.txt', 'r') as input_file:
#     content = input_file.readlines()
#     for line in content:

#         dog_data = line.split()
#         dogs_dict[dog_data[0]] = {'id' : dog_data[0], 'breed' : dog_data[1],
#                                   'name' : dog_data[2]}


# def delete_from_file(id):
#     with open('shelter.txt', 'w') as output_file:
#         new_shelter_list = ''
#         for dog_id in dogs_dict:
#             if dog_id != id:

#                 new_shelter_list += dogs_dict[dog_id]['id'] + ' ' + \
#                                     dogs_dict[dog_id]['breed'] + ' ' + \
#                                     dogs_dict[dog_id]['name'] + '\n'
#         output_file.write(new_shelter_list)

# def write_to_file(new_doggo):
#     with open('shelter.txt', 'a') as output_file:
#         output_file.write(new_doggo)



@app.route('/')
def hello():
	return'Welcome to the puppy shelter'

# @app.route('/list_dogs')
# def list_dogs():
# 	dogs_string = ''
# 	for key in dogs_dict:
# 		dogs_string += dogs_dict[key]['breed'] + ' named ' +  dogs_dict[key]['name']
# 		dogs_string += '\n'
# 	return'These are our pupps:\n{}'.format(dogs_string)


@app.route('/dogs_db/dogs', methods=['GET'])
def get_all_dogs():
	return jsonify({'Our Pupps':dogs_db})


@app.route('/dogs_db/dogs/<dog_id>', methods=['DELETE'])
def adopt_dog(dog_id):
	adopted_dog = [ dog for dog in dogs_db if (dog['id'] == dog_id)]
	if len(adopted_dog) == 0:
		abort(404)
	dogs_db.remove(adopted_dog[0])
	return 'Your adopted pup:\n', jsonify({'puppy':adopted_dog[0]})



# @app.route('/adoption')
# def adoption():
# 	dog_ID = request.args.get('dog_ID', default = None, type = 'str')
#     if dog_ID in dogs_dict:
#         adoption_protocol = "You adopted a pup! It's breed is {} and it's name is {}.\n" \
#                             "There will be more sunshine!".format(dogs_dict[id]['breed'],
#                                                                   dogs_dict[id]['name'])
#         del dogs_dict[dog_ID]
#         delete_from_file(dog_ID)
#     else:
#         adoption_protocol = "There is no such pup in the shelter. Look at our other cuties"

#     return adoption_protocol


@app.route('/dogs_db/dogs', methods=['POST'])
def give_away_dog():
	new_dog = {
	'id' : request.json['id'],
	'breed' : request.json['breed'],
	'name' : request.json['name']
	}
	dogs_db.append(new_dog)
	return'That was very cruel! Shame on you.', jsonify(new_dog)



# @app.route('/dogs_db/dogs', methods=['POST'])
# def give_away_dog():
# 	current_ID = int(dog_id_list[-1])
#     new_ID = current_ID + 1
#     breed = request.args.get('breed', default = None, type = 'str')
#     name = request.args.get ('name', default = None, type = 'str')

#     new_doggo = str(new_ID) + ' ' + breed + ' ' + name

#     write_to_file('\n{}'.format(new_doggo))
# 	return'That was very cruel! Shame on you.'

if __name__ == "__main__":
	# dog_shelter.run(host="0.0.0.0", debug=True)
	app.run()

