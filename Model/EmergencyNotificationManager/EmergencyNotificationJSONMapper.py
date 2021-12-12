from DTO.XEmergencyNotification import XEmergencyNotification
from Utils.APIException import APIException


class EmergencyNotificationJSONMapper:

    def dto_to_json(self, x_emergency_notification):
        return {
            "emergency_id": x_emergency_notification.emergency_id,
            "emergency_status": x_emergency_notification.emergency_status,
            "sensor_id": x_emergency_notification.sensor_id,
            "emergency_type": x_emergency_notification.emergency_type
        }

    def json_to_dto(self, json):
        emergency_id = json.get("emergency_id")
        emergency_status = json.get("emergency_status")
        sensor_id = json.get("sensor_id")
        emergency_type = json.get("emergency_type")
        if not emergency_status:
            return APIException("Emergency status must not be empty!", 422)
        if not sensor_id:
            return APIException("Sensor id must not be empty!", 422)
        if not emergency_type:
            return APIException("Emergency type must not be empty!", 422)
        return XEmergencyNotification(
            emergency_id,
            emergency_status,
            sensor_id,
            emergency_type
        )