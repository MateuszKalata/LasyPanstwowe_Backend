from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mpmnyhpdqfkysz:74fb1cea523c76029effb7c4638410e83d1c66f7a292a8495563dc68dd2d9efc@ec2-54-74-95-84.eu-west-1.compute.amazonaws.com:5432/d7jfim7rcp2eq3'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Sensor(db.Model):
    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    administrator = db.Column(db.String(200))
    dateAdded = db.Column(db.String(200))
    forestAreaId = db.Column(db.String(200))
    name = db.Column(db.String(200))
    status = db.Column(db.String(200))
    type = db.Column(db.String(200))
    unit = db.Column(db.String(200))


    def __init__(self,administrator,dateAdded, forestAreaId, name, status, type, unit):
        self.administrator = administrator
        self.dateAdded = dateAdded
        self.forestAreaId = forestAreaId
        self.name = name
        self.status = status
        self.type = type
        self.unit = unit

class XSensor():
    def __init__(self,administrator,dateAdded, forestAreaId, id, name, status, type, unit):
        self.administrator = administrator
        self.dateAdded = dateAdded
        self.forestAreaId = forestAreaId
        self.id = id
        self.name = name
        self.status = status
        self.type = type
        self.unit = unit

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':

        administrator = request.form['administrator']
        name = request.form['name']
        dateAdded = request.form['dateAdded']
        forestAreaId = request.form['forestAreaId']
        status = request.form['status']
        type = request.form['type']
        unit = request.form['unit']

        if db.session.query(Sensor).filter(Sensor.name == name).count() == 0:
            data = Sensor(administrator, dateAdded, forestAreaId, name, status, type, unit)
            db.session.add(data)
            db.session.commit()
            return 'super'
        return 'niesuper'


# class SensorRESTController():

# name - zmienic na ID
@app.route('/send/sensor', methods = ['GET'])
def sendSensor():
    if request.method == 'GET':
        name = request.args.get('name')
        
        search = Sensor.query.filter_by(name=name).first()
        xSensor = XSensor(search.administrator, search.dateAdded, search.forestAreaId, search.id, search.name, search.status, search.type, search.unit)
        resultJson = json.dumps(xSensor.__dict__)
        return resultJson

#zwracac liste
@app.route('/send/sensorByForestry', methods = ['GET'])
def sendSensorByForestry():
    if request.method == 'GET':
        forestAreaId = request.args.get('forestAreaId')
        
        search = Sensor.query.filter_by(forestAreaId=forestAreaId)
        xSensorList = []
        for singeSensor in search:
            xSensor = XSensor(singeSensor.administrator, singeSensor.dateAdded, singeSensor.forestAreaId, singeSensor.id, singeSensor.name, singeSensor.status, singeSensor.type, singeSensor.unit)
            xSensorList.append(json.dumps(xSensor.__dict__))
        resultJson = json.dumps(xSensorList)
        return resultJson

#zwracac liste
@app.route('/send/sensorNotAssinged', methods = ['GET'])
def sendSensorNotAssigned():
    if request.method == 'GET':
        
        search = Sensor.query.filter_by(forestAreaId=None)
        xSensorList = []
        for singeSensor in search:
            xSensor = XSensor(singeSensor.administrator, singeSensor.dateAdded, singeSensor.forestAreaId, singeSensor.id, singeSensor.name, singeSensor.status, singeSensor.type, singeSensor.unit)
            xSensorList.append(json.dumps(xSensor.__dict__))
        resultJson = json.dumps(xSensorList)
        return resultJson

@app.route('/send/assignSensor', methods = ['PATCH'])
def assignSensor():
    if request.method == 'PATCH':
   
        forestAreaId = request.form.get("forestAreaId")
        name = request.form.get("name")
        
        search = Sensor.query.filter_by(name=name).first()
        search.forestAreaId = forestAreaId
        db.session.add(search)
        db.session.commit()
        return 'poszlo'


if __name__ == '__main__':
    app.run()
