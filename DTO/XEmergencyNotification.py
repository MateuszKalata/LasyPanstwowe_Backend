class XEmergencyNotification:
    def __init__(self, emergency_id, emergency_status, sensor_id, emergency_type, emergency_timestamp, emergency_value):
        self.emergency_id = emergency_id
        self.emergency_status = emergency_status
        self.sensor_id = sensor_id
        self.emergency_type = emergency_type
        self.emergency_timestamp = emergency_timestamp
        self.emergency_value = emergency_value
