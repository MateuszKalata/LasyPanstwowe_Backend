class XEmergencyNotification:
    def __init__(self, id, status, sensor_id, type, measurements):
        self.id = id
        self.status = status
        self.sensor_id = sensor_id
        self.type = type
        self.measurements = measurements
