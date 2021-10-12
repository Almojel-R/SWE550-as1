from flask import Flask, render_template, request
import pymongo
from pymongo import MongoClient
from flask import jsonify 
from bson import ObjectId # For ObjectId to work    


app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["studentID_db"]
    return db

@app.route('/')
def ping_server():
    return render_template("index.html")

@app.route('/findstudent' , methods=['GET'])   
def find_student():
    id = request.values.get("studentID") 
    db=""
    try:
        db = get_db()
        student = db.studentID_tb.find_one({'id':id})
        name = student["name"]
        mark = student["mark"] 
        studentid =  student["id"] 
        return render_template("index.html", name=name, mark=mark, studentid=studentid)
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/students')
def get_sudents():
    db=""
    try:
        db = get_db()
        _animals = db.studentID_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "mark": animal["mark"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)