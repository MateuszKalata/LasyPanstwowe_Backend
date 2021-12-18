from DTO.XEmergencyNotification import XEmergencyNotification
from DTO.XSensorMeasurement import XSensorMeasurement
from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity


class EmergencyNotificationMapper:

    def entity_to_dto(self, emergency_notification_entity):
        return XEmergencyNotification(
            emergency_notification_entity.id,
            emergency_notification_entity.status,
            emergency_notification_entity.sensor_id,
            emergency_notification_entity.type,
            [XSensorMeasurement(
                measurement.id,
                measurement.sensor_id,
                measurement.timestamp,
                measurement.value
            ) for measurement in emergency_notification_entity.sensor_measurements]
        )

    def dto_to_entity(self, x_emergency_notification):
        return EmergencyNotificationEntity(
            x_emergency_notification.id,
            x_emergency_notification.status,
            x_emergency_notification.sensor_id,
            x_emergency_notification.type,
        )
