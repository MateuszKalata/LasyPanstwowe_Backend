from DTO.XEmergencyNotification import XEmergencyNotification
from DTO.XSensorMeasurement import XSensorMeasurement
from Data.SensorMeasurementRepository.SensorMeasurementMapper import SensorMeasurementMapper
from Data.SensorRepository.SensorMapper import SensorMapper
from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity


class EmergencyNotificationMapper:

    def __init__(self):
        self.sensor_measurement_mapper = SensorMeasurementMapper()
        self.sensor_mapper = SensorMapper()

    def entity_to_dto(self, emergency_notification_entity: EmergencyNotificationEntity):
        return XEmergencyNotification(
            emergency_notification_entity.id,
            emergency_notification_entity.status,
            emergency_notification_entity.sensor_id,
            emergency_notification_entity.type,
            emergency_notification_entity.timestamp,
            [self.sensor_measurement_mapper.convert_sensor_measurement_entity_to_xsensormeasurement(measurement)
             for measurement in emergency_notification_entity.sensor_measurements],
            emergency_notification_entity.sensor.forest_area.forestry.name,
            emergency_notification_entity.sensor.forest_area.name,
            self.sensor_mapper.convertSensorEntityToXSensor(emergency_notification_entity.sensor)
        )

    def dto_to_entity(self, x_emergency_notification):
        return EmergencyNotificationEntity(
            x_emergency_notification.id,
            x_emergency_notification.status,
            x_emergency_notification.sensor_id,
            x_emergency_notification.type
        )
