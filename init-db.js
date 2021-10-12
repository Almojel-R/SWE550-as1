db = db.getSiblingDB("studentID_db");
db.studentID_tb.drop();

db.studentID_tb.insertMany([
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
    }
]);