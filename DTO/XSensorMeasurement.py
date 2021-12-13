class XSensorMeasurement:
    def __init__(self, id, sensor_id, sensor_name, value, unit, date, is_critical):
        self.id = id
        self.sensor_id = sensor_id
        self.sensor_name = sensor_name
        self.value = value
        self.unit = unit
        self.date = date
        self.is_critical = is_critical

    def as_dict(self):
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "sensor_name": self.sensor_name,
            "value": self.value,
            "unit": self.unit,
            "date": self.date,
            "is_critical": self.is_critical
        }
