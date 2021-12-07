from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class EmergencyNotificationEntity(Base):
    __tablename__ = 'emergency_notifications'

    id = Column(Integer, primary_key=True)
    emergency_status = Column(String(200))
    sensor_id = Column(Integer)
    emergency_type = Column(String(200))

    def __init__(self, id, emergency_status, sensor_id, emergency_type):
        self.id = id
        self.emergency_status = emergency_status
        self.sensor_id = sensor_id
        self.emergency_type = emergency_type
