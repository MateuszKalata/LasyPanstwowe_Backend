class XSensorMeasurement:
    def __init__(self, id, sensor_id, timestamp, value, emergency_notification_id=None):
        self.id = id
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.emergency_notification_id = emergency_notification_id

    def as_dict(self):
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "sensor_name": self.timestamp,
            "value": self.value,
        }
