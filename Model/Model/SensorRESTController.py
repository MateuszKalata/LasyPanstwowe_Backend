# zostawić tutaj tylko komunikacje z klientem
from flask import Blueprint, request, jsonify
from DTO.XSensor import XSensor
from SensorManager import SensorManager


sensors_controller = Blueprint('SensorRESTController',__name__)
sensorMenager = SensorManager()

def __init__(self, SensoreManager):
    self.ISensors = SensoreManager

@sensors_controller.route('/submit/<id>', methods=['POST'])
def submit(id):
    xsensor = XSensor(
        request.json.get('administrator'),
        request.json.get('data_added'),
        request.json.get('forest_area_id'),
        None,
        request.json.get('name'),
        request.json.get('status'),
        request.json.get('type'),
        request.json.get('unit')
    )
    status = sensorMenager.RegisterSensor(xsensor)
    return status

@sensors_controller.route('/send/sensor/<id>', methods = ['GET'])
def sendSensor(id):
    xSensor = sensorMenager.GetSensor(int(id))
    if xSensor == 1:
        return "not found", 404
    return jsonify([xSensor.as_dict()]),200

@sensors_controller.route('/send/sensorByForestry/<id>', methods = ['GET'])
def sendSensorByForestry(id):
    xSensors = sensorMenager.GetSensorsByForestry(int(id))
    if xSensors == 1:
        return "not found", 404
    return jsonify([xSensor.as_dict() for xSensor in xSensors]),200

@sensors_controller.route('/send/sensorNotAssinged', methods = ['GET'])
def sendSensorNotAssigned():
    xSensors = sensorMenager.GetSensorsNotAssigned()
    if xSensors == 1:
        return "not found", 404
    return jsonify([xSensor.as_dict() for xSensor in xSensors]),200

@sensors_controller.route('/send/assignSensor', methods = ['PATCH'])
def assignSensor():
    idForestArea = int(request.json.get('forest_area_id'))
    idSensor = int(request.json.get('sensor_id'))
    status = sensorMenager.AssignSensor(idSensor,idForestArea)
    return str(status), 200




