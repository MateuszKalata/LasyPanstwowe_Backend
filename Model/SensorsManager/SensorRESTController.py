# zostawić tutaj tylko komunikacje z klientem
import re
from flask import Blueprint, request, jsonify
from DTO.XSensor import XSensor
from Model.SensorsManager.SensorManager import SensorManager
from Model.ForestryManager.ForestriesImpl import ForestriesImpl
from datetime import datetime


sensors_controller = Blueprint('SensorRESTController',__name__)
sensorMenager = SensorManager()
forestriesImpl = ForestriesImpl()

def __init__(self, SensoreManager):
    self.ISensors = SensoreManager

@sensors_controller.route('/sensor', methods=['POST'])
def submit():
    xsensor = XSensor(
        request.json.get('administrator'),
        datetime.now().isoformat(),
        request.json.get('forest_area_id'),
        None,
        request.json.get('name'),
        request.json.get('status'),
        request.json.get('type'),
        request.json.get('unit'),
        request.json.get('longitude'),
        request.json.get('latitude')
    )
    #test czy potrzebne dane są liczbą
    if (not isNumber(xsensor.longitude) or not isNumber(xsensor.latitude)):
        return "longitude, latitude should be numbers" , 422
    elif (not xsensor.forestAreaId == "" and not xsensor.forestAreaId.isdigit()):
        return "forest_area_id should be positive integer" , 422
    id = sensorMenager.RegisterSensor(xsensor)
    if id == -1:
        return "Bad sensore type. Allowed types: fire, humidity, rain, wind, temperature, camera, camera_trap" , 422
    elif id == -2:
        return "Bad unit. Allowed types: empty, %, K, C, F, °C, °F, bool, m/s, km/h, mm", 422
    return {"id": str(id)}, 200

@sensors_controller.route('/sensor', methods = ['GET'])
def sendSensor():
    id = request.args.get('id')
    if (not id.isdigit()):
        return "id should be positive integer" , 422
    xSensor = sensorMenager.GetSensor(id)
    if xSensor == 1:
        return "not found", 404
    return jsonify(xSensor.as_dict()),200

@sensors_controller.route('/sensors', methods = ['GET'])
def sendSensorByForestry():
    forestry_id = request.args.get('forestry_id')
    if (not forestry_id.isdigit()):
        return "forestry_id should be positive integer" , 422
    forestryAreasList = forestriesImpl.get_forest_areas(int(request.args.get('forestry_id')))
    sensorLists = [sensorMenager.GetSensorsByForestry(str(forestryArea.id)) for forestryArea in forestryAreasList]
    return jsonify([sensor.as_dict() for sensorList in sensorLists for sensor in sensorList]), 200

@sensors_controller.route('/sensors_not_assinged', methods = ['GET'])
def sendSensorNotAssigned():
    xSensors = sensorMenager.GetSensorsNotAssigned()
    if xSensors == 1:
        return "not found", 404
    return jsonify([xSensor.as_dict() for xSensor in xSensors]), 200

@sensors_controller.route('/assign_sensor', methods = ['PATCH'])
def assignSensor():
    idForestArea = request.args.get('forest_area_id')
    name = request.args.get('id')
    if (not name.isdigit() or not idForestArea.isdigit()):
        return "id, forest_area_id should be positive integers" , 422
    status = sensorMenager.AssignSensor(name,idForestArea)
    return str(status), 200

    
@sensors_controller.route('/activate_sensor', methods = ['PATCH'])
def activateSensor():
    id = request.args.get('id')
    if not id.isdigit():
        return "id should be positive integers" , 422
    status = sensorMenager.ActivateSensor(id)
    return str(status), 200

def isNumber(str):
    return re.match(r"[-+]?\d+(\.\d*)?$", str) is not None



