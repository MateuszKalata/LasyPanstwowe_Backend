from DTO.XEmergencyNotification import XEmergencyNotification
from Utils.APIException import APIException


class EmergencyNotificationJSONMapper:

    def dto_to_json(self, x_emergency_notification):
        return {
            "emergency_id": x_emergency_notification.emergency_id,
            "emergency_status": x_emergency_notification.emergency_status,
            "sensor_id": x_emergency_notification.sensor_id,
            "emergency_type": x_emergency_notification.emergency_type,
            "measurements": [{
                "timestamp": measurement.get("timestamp"),
                "value": measurement.get("value")
            } for measurement in x_emergency_notification.measurements]
        }

    def json_to_dto(self, json):

        emergency_id = None
        sensor_id = json.get("sensor_id")
        emergency_type = json.get("emergency_type")
        emergency_status = json.get("emergency_status")
        if not emergency_status:
            raise APIException("Emergency status must not be empty!", 422)
        if not sensor_id:
            raise APIException("Sensor id must not be empty!", 422)
        if not emergency_type:
            raise APIException("Emergency type must not be empty!", 422)

        return XEmergencyNotification(
            emergency_id,
            emergency_status,
            sensor_id,
            emergency_type,
            json.get("sensor_measurements")
        )
