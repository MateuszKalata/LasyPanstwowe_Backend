from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class EmergencyNotificationEntity(Base):
    __tablename__ = 'emergency_notifications'

    id = Column(Integer, primary_key=True)
    emergency_id = Column(Integer)
    emergency_status = Column(Integer)
    sensor_id = Column(Integer)
    emergency_type = Column(Integer)
    emergency_timestamp = Column(String(50))
    emergency_value = Column(Integer)

    def __init__(self, emergency_id, emergency_status, sensor_id, emergency_type, emergency_timestamp, emergency_value):
        self.emergency_id = emergency_id
        self.emergency_status = emergency_status
        self.sensor_id = sensor_id
        self.emergency_type = emergency_type
        self.emergency_timestamp = emergency_timestamp
        self.emergency_value = emergency_value
