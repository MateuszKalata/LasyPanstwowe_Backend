from DTO.XSensorMeasurement import XSensorMeasurement
from Entities.SensorMeasurementEntity import SensorMeasurementEntity


class SensorMeasurementMapper:

    def convert_sensor_measurement_entity_to_xsensormeasurement(self, sensor_measurement_entity):
        return XSensorMeasurement(
            sensor_measurement_entity.id,
            sensor_measurement_entity.sensor_id,
            sensor_measurement_entity.timestamp,
            sensor_measurement_entity.value,
        )

    def convert_xsensormeasurement_to_sensor_measurement_entity(self, xsensormeasurement):
        return SensorMeasurementEntity(
            xsensormeasurement.id,
            xsensormeasurement.sensor_id,
            xsensormeasurement.timestamp,
            xsensormeasurement.value,
        )
