from DTO.XEmergencyNotification import XEmergencyNotification
from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity

class EmergencyNotificationMapper:

    def convert_xemergency_notification_to_emergency_notification_entity(self, xemergency):
        return EmergencyNotificationEntity(
            xemergency.id,
            xemergency.emergency_status,
            xemergency.sensor_id,
            xemergency.emergency_type
        )

    def convert_emergency_notification_entity_to_xemergency_notification(self, emergency_entity):
        return XEmergencyNotification(
            emergency_entity.id,
            emergency_entity.emergency_status,
            emergency_entity.sensor_id,
            emergency_entity.emergency_type
        )