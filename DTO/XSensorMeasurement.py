class XSensorMeasurement:
    def __init__(self, id, sensor_id, sensor_name, value, unit, date):
        self.id = id
        self.sensor_id = sensor_id
        self.sensor_name = sensor_name
        self.value = value
        self.unit = unit
        self.date = date

    def as_dict(self):
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "sensor_name": self.sensor_name,
            "value": self.value,
            "unit": self.unit,
            "date": self.date
        }
