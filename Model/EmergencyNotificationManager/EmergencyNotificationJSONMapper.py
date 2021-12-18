from DTO.XEmergencyNotification import XEmergencyNotification
from DTO.XSensorMeasurement import XSensorMeasurement
from Utils.APIException import APIException


class EmergencyNotificationJSONMapper:

    def dto_to_json(self, x_emergency_notification):
        return {
            "emergency_id": x_emergency_notification.id,
            "emergency_status": x_emergency_notification.status,
            "sensor_id": x_emergency_notification.sensor_id,
            "emergency_type": x_emergency_notification.type,
            "measurements": [{
                "timestamp": measurement.timestamp,
                "value": measurement.value
            } for measurement in x_emergency_notification.measurements]
        }

    def json_to_dto(self, json):

        id = None
        sensor_id = json.get("sensor_id")
        type = json.get("emergency_type")
        status = json.get("emergency_status")
        if not status:
            raise APIException("Emergency status must not be empty!", 422)
        if not sensor_id:
            raise APIException("Sensor id must not be empty!", 422)
        if not type:
            raise APIException("Emergency type must not be empty!", 422)

        return XEmergencyNotification(
            id,
            status,
            sensor_id,
            type,
            [XSensorMeasurement(
                None,
                sensor_id,
                measurement.get("timestamp"),
                measurement.get("value"),
                None
            ) for measurement in json.get("measurements")]
        )
