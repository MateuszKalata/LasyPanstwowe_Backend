# zostawić tutaj tylko komunikacje z klientem
from flask import Blueprint, request, jsonify
from DTO.XSensor import XSensor
from Model.SensorsManager.SensorManager import SensorManager
from Model.ForestryManager.ForestriesImpl import ForestriesImpl


sensors_controller = Blueprint('SensorRESTController',__name__)
sensorMenager = SensorManager()
forestriesImpl = ForestriesImpl()

def __init__(self, SensoreManager):
    self.ISensors = SensoreManager

@sensors_controller.route('/sensor', methods=['POST'])
def submit():
    xsensor = XSensor(
        request.form.get('administrator'),
        request.form.get('date_added'),
        request.form.get('forest_area_id'),
        None,
        request.form.get('name'),
        request.form.get('status'),
        request.form.get('type'),
        request.form.get('unit')
    )
    id = sensorMenager.RegisterSensor(xsensor)
    return {"id": str(id)}, 200

@sensors_controller.route('/sensor', methods = ['GET'])
def sendSensor():
    xSensor = sensorMenager.GetSensor(request.args.get('id'))
    if xSensor == 1:
        return "not found", 404
    return jsonify([xSensor.as_dict()]),200

@sensors_controller.route('/sensors', methods = ['GET'])
def sendSensorByForestry():
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
    name = request.args.get('name')
    status = sensorMenager.AssignSensor(name,idForestArea)
    return str(status), 200




