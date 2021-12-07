class XEmergencyNotification:
    def __init__(self, id, emergency_status, sensor_id, emergency_type):
        self.id = id
        self.emergency_status = emergency_status
        self.sensor_id = sensor_id
        self.emergency_type = emergency_type

    def as_dict(self):
        return {
            "id": self.id,
            "emergency_status" : self.emergency_status,
            "sensor_id" : self.sensor_id,
            "emergency_type" : self.emergency_type
        }
