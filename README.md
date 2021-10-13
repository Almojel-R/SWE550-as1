# SWE550 assignment 1

This is simple application of micro-service architecture. 

## Built using 
* Language: python 
* Framework: Flask
* Database: mongo db 
* Container: Docker
 
## The project contain the following  files: 
* app.py 
* index.html
* init-db.js 
* docker-compose.yml
* Dockerfile
* requirement.txt
 
 ## database 
 
```json 
studentID_tb = ([
    {
        "id": "4352020",
        "name": "Raghad", 
        "mark": "10" 
    },
    {
        "id": "4371010",
        "name": "Reema",
        "mark": "10" 
    },
    {
        "id": "442020",
        "name": "Aziza",
        "mark": "10" 
    }])
  ```
  
## The result of the project: 
* Container 1: app
* Container 2 :  mongo db 
* Communication method: Rest API


Credit: to [Dev Sense](https://www.youtube.com/channel/UC_amoXmmxSY9KusoDczDTXQ) for providing a tutorial for building dockerized app.
