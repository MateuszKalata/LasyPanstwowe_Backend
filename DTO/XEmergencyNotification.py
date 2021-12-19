class XEmergencyNotification:
    def __init__(self, id, status, sensor_id, type, timestamp, measurements, forestry_name=None, forest_area_name=None, sensor=None):
        self.id = id
        self.status = status
        self.sensor_id = sensor_id
        self.type = type
        self.timestamp = timestamp
        self.measurements = measurements
        self.forestry_name = forestry_name
        self.forest_area_name = forest_area_name
        self.sensor = sensor
