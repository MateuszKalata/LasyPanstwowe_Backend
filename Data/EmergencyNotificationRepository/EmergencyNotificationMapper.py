from DTO.XEmergencyNotification import XEmergencyNotification
from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity


class EmergencyNotificationMapper:

    def entity_to_dto(self, emergency_notification_entity):
        return XEmergencyNotification(
            emergency_notification_entity.emergency_id,
            emergency_notification_entity.emergency_status,
            emergency_notification_entity.sensor_id,
            emergency_notification_entity.emergency_type
        )

    def dto_to_entity(self, x_emergency_notification):
        return EmergencyNotificationEntity(
            x_emergency_notification.emergency_id,
            x_emergency_notification.emergency_status,
            x_emergency_notification.sensor_id,
            x_emergency_notification.emergency_type
        )
