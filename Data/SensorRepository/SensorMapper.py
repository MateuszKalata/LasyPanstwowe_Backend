from DTO.XSensor import XSensor
from Entities.SensorEntity import SensorEntity


class SensorMapper:

    def convertSensorEntityToXSensor(self, sensorEntity):
        return XSensor(
            sensorEntity.administrator,
            sensorEntity.dateAdded,
            sensorEntity.forestAreaId,
            sensorEntity.id,
            sensorEntity.name,
            sensorEntity.status,
            sensorEntity.type,
            sensorEntity.unit,
            sensorEntity.longitude,
            sensorEntity.latitude
        )

    def convertXSensorToSensorEntity(self, xSensor):
        return SensorEntity(
            xSensor.administrator,
            xSensor.dateAdded,
            xSensor.forestAreaId,
            xSensor.name,
            xSensor.status,
            xSensor.type,
            xSensor.unit,
            xSensor.longitude,
            xSensor.latitude
        )
