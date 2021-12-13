from DTO.XEmergencyNotification import XEmergencyNotification
from Utils.APIException import APIException


class EmergencyNotificationJSONMapper:

    def dto_to_json(self, x_emergency_notification):
        return {
            "emergency_id": x_emergency_notification.emergency_id,
            "emergency_status": x_emergency_notification.emergency_status,
            "sensor_id": x_emergency_notification.sensor_id,
            "emergency_type": x_emergency_notification.emergency_type,
            "emergency_timestamp": x_emergency_notification.emergency_timestamp,
            "emergency_value": x_emergency_notification.emergency_value
        }

    def json_to_dto(self, json):
        if len(json.get("sensor_measurements")) < 3:
            raise APIException(
                "There have to be at leat 3 sensor measurements!", 422)

        emergency_id = json.get("emergency_id")
        sensor_id = json.get("sensor_id")
        emergency_type = json.get("emergency_type")
        emergency_status = json.get("emergency_status")
        if not emergency_status:
            raise APIException("Emergency status must not be empty!", 422)
        if not sensor_id:
            raise APIException("Sensor id must not be empty!", 422)
        if not emergency_type:
            raise APIException("Emergency type must not be empty!", 422)

        emergency_arr = []
        for emergency_measurement in json.get("sensor_measurements"):
            if not emergency_measurement.get("timestamp"):
                raise APIException("Emergency timestamp must not be empty!", 422)
            if not emergency_measurement.get("value"):
                raise APIException("Emergency value must not be empty!", 422)

            emergency_arr.append(XEmergencyNotification(
                emergency_id,
                emergency_status,
                sensor_id,
                emergency_type,
                emergency_measurement.get("timestamp"),
                emergency_measurement.get("value")
            )
            )
            emergency_id += 1

        return emergency_arr
