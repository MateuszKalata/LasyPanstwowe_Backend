from Data.SensorMeasurementRepository.SensorMeasurementRepository import SensorMeasurementRepository
from Model.SensorMeasurementManager.ISensorMeasurementReporting import ISensorMeasurementReporting
from Model.SensorMeasurementManager.ISensorMeasurements import ISensorMeasurements


class SensorMeasurementManager(ISensorMeasurementReporting, ISensorMeasurements):

    def __init__(self):
        self.sensor_measurement_repository = SensorMeasurementRepository()

    def report_measurement(self, measurement):
        return self.sensor_measurement_repository.create(measurement)

    def get_all(self):
        return self.sensor_measurement_repository.read_all()

    def get_measurements_by_sensor_id(self, id):
        return self.sensor_measurement_repository.read_id(id)
