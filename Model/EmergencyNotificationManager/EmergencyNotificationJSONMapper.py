from DTO.XEmergencyNotification import XEmergencyNotification
from DTO.XSensorMeasurement import XSensorMeasurement
from Utils.APIException import APIException


class EmergencyNotificationJSONMapper:

    def dto_to_json(self, x_emergency_notification: XEmergencyNotification):
        return {
            "emergency_id": x_emergency_notification.id,
            "emergency_status": x_emergency_notification.status,
            "measurements": [measurement.as_dict()
                             for measurement in x_emergency_notification.measurements],
            "forestry_name": x_emergency_notification.forestry_name,
            "forest_area_name": x_emergency_notification.forest_area_name,
            "sensor": x_emergency_notification.sensor.as_dict(),
            "timestamp": x_emergency_notification.timestamp
        }

    def json_to_dto(self, json):

        id = None
        sensor_id = json.get("sensor_id")
        status = json.get("emergency_status")
        if not status:
            raise APIException("Emergency status must not be empty!", 422)
        if not sensor_id:
            raise APIException("Sensor id must not be empty!", 422)

        return XEmergencyNotification(
            id,
            status,
            sensor_id,
            0,
            None,
            [XSensorMeasurement(
                None,
                sensor_id,
                measurement.get("timestamp"),
                measurement.get("value"),
                None
            ) for measurement in json.get("measurements")]
        )
