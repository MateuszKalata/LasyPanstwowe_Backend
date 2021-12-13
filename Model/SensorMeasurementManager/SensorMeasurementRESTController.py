from flask import Blueprint, request
from Model.SensorMeasurementManager.SensorMeasurementManager import SensorMeasurementManager
from DTO.XSensorMeasurement import XSensorMeasurement
import json

sensor_measurement_controller = Blueprint('SensorMeasurementRESTController', __name__)
sensor_manager = SensorMeasurementManager()


@sensor_measurement_controller.route("/measurements", methods=['POST'])
def add_measurement():
    xmeasurement = XSensorMeasurement(
        None,
        request.json.get('sensor_id'),
        request.json.get('sensor_name'),
        request.json.get('value'),
        request.json.get('unit'),
        request.json.get('date'),
        request.json.get('is_critical')
    )
    id = sensor_manager.report_measurement(xmeasurement)
    return {"id": str(id)}, 200


@sensor_measurement_controller.route("/measurements", methods=['GET'])
def get_measurements():
    xmeasurements = sensor_manager.get_all()
    xmeasurements = [xmeasurement.as_dict() for xmeasurement in xmeasurements]
    return json.dumps(xmeasurements), 200


@sensor_measurement_controller.route("/measurements/<id>", methods=['GET'])
def get_measurements_by_sensor_id(id):
    xmeasurements = sensor_manager.get_measurements_by_sensor_id(id)
    xmeasurements = [xmeasurement.as_dict() for xmeasurement in xmeasurements]
    return json.dumps(xmeasurements), 200
