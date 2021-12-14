class XSensorMeasurement:
    def __init__(self, id, sensor_id, timestamp, value):
        self.id = id
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value

    def as_dict(self):
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "sensor_name": self.timestamp,
            "value": self.value,
        }
