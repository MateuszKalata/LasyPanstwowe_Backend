from flask import Blueprint, request
from Model.SensorMeasurementManager.SensorMeasurementManager import SensorMeasurementManager
from DTO.XSensorMeasurement import XSensorMeasurement
from Model.SensorsManager.SensorManager import SensorManager
import json

sensor_measurement_controller = Blueprint('SensorMeasurementRESTController', __name__)
sensor_measurements_manager = SensorMeasurementManager()
sensor_manager = SensorManager()


@sensor_measurement_controller.route("/measurements", methods=['POST'])
def add_measurement():
    xmeasurement = XSensorMeasurement(
        None,
        request.json.get('sensor_id'),
        request.json.get('timestamp'),
        request.json.get('value'),
    )
    if xmeasurement.sensor_id is None or xmeasurement.timestamp is None or xmeasurement.value is None:
        return "Invalid and/or missing measurement data", 400

    sensor = sensor_manager.GetSensor(xmeasurement.sensor_id)
    print("sensor:")
    print(sensor)
    if sensor == 1:
        return "There is no sensor with id " + str(xmeasurement.sensor_id) + ".", 404
    id = sensor_measurements_manager.report_measurement(xmeasurement)
    return "Measurement with id " + str(id) + " created.", 201


@sensor_measurement_controller.route("/measurements", methods=['GET'])
def get_measurements():
    xmeasurements = sensor_measurements_manager.get_all()
    xmeasurements = [xmeasurement.as_dict() for xmeasurement in xmeasurements]
    return json.dumps(xmeasurements), 200


@sensor_measurement_controller.route("/measurements/<id>", methods=['GET'])
def get_measurements_by_sensor_id(id):
    xmeasurements = sensor_measurements_manager.get_measurements_by_sensor_id(id)
    xmeasurements = [xmeasurement.as_dict() for xmeasurement in xmeasurements]
    return json.dumps(xmeasurements), 200
