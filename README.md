# Dog-shelter
Web service using python flask

### Running
You need to have docker and docker-compose installed

To build and run:

docker-compose build

docker-compose up -d

Port 5000 is used.

### Possible querys from terminal

1) GET the list of dogs:

curl -i http://localhost:5000/dogs_db/dogs

2) DELETE (adopt) a dog from existing dogs_db (<dog_id> is the id of a dog from the database):

curl -i -X DELETE http://localhost:5000/dogs_db/dogs/<dog_id>

3) POST (give away) your dog to a shelter:

curl -i -X POST -H "Content-Type: application/json" -d '{ "id": "<dog_id>, "breed": "<dog_breed>", "name": "<dog_name>"}' http://localhost:5000/dogs_db/dogs


### Query examples

2) curl -i -X DELETE http://localhost:5000/dogs_db/dogs/2

3) curl -i -X POST -H "Content-Type: application/json" -d '{ "id": "6", "breed": "Yorkshire Terriere", "name": "Lily"}' http://localhost:5000/dogs_db/dogs