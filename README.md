# Dog-shelter
Web service using python flask

## FIRST task
### Running
You need to have docker and docker-compose installed

To build and run:

docker-compose build

docker-compose up -d

Port 5000 is used.

### Possible queries from terminal for 1st task

1. GET the list of dogs:
```
curl -i http://localhost:5000/dogs
```  
2. DELETE (adopt) a dog from existing dogs_db (<dog_id> is the id of a dog from the database):
```
curl -i -X DELETE http://localhost:5000/dogs/<dog_id>
```  
3. POST (give away) your dog to a shelter:
```
curl -i -X POST -H "Content-Type: application/json" -d '{ "id": "<dog_id>, "breed": "<dog_breed>"}' http://localhost:5000/dogs/<give_away_dog_name>
```
4. PUT (become a guardian)
```
curl -i -H "Content-type: application/json" -X PUT -d "{\"temporary guardian"\":\"<guardian_name>\"}" http://localhost:5000/dogs/<dog_id>
```


### Query examples

2. ```curl -i -X DELETE http://localhost:5000/dogs/2```

3. ```curl -i -X POST -H "Content-Type: application/json" -d '{ "id": "6", "breed": "Yorkshire Terriere"}' http://localhost:5000/dogs/"Lily"```

4. ```curl -i -H "Content-type: application/json" -X PUT -d "{\"temporary guardian\":\"John Doe\"}" http://localhost:5000/dogs/1```

## SECOND task
### Running
You need to have docker and docker-compose installed  
To build and run:

cd 2nd  

docker-compose build  

docker-compose up -d  
  
Ports 5000 and 81 are used for the services.  

### Queries for the second task
1. GET all visits from the used web service:
```
curl -i http://localhost:5000/visits
```  
2. GET visits that belong to the dog by its guardians ID
```
curl -i http://localhost:5000/dogs/<dog_id>/visits
```  
3. POST a new visit and add it to the list of visits of the dog
```
curl -i -X POST http://localhost:5000/dogs/<dog_id>/visits
```
4. DELETE an exisiting visit from the visit service and from the dogs' list of visits by the visit ID
```
curl -i -X DELETE http://localhost:5000/dogs/<dog_id>/visits/<visit_id>
```  

### Query examples

2. 
```
curl -i http://localhost:5000/dogs/4/visits
```  

3.
```
curl -i -X POST http://localhost:5000/dogs/4/visits
```

4.
```
curl -i -X DELETE http://localhost:5000/dogs/4/visits/1
```  