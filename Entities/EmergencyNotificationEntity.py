from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


class EmergencyNotificationEntity(Base):
    __tablename__ = 'emergency_notifications'

    emergency_id = Column(Integer, primary_key=True)
    emergency_status = Column(Integer)
    sensor_id = Column(Integer)
    emergency_type = Column(Integer)

    def __init__(self, emergency_id, emergency_status, sensor_id, emergency_type):
        self.emergency_id = emergency_id
        self.emergency_status = emergency_status
        self.sensor_id = sensor_id
        self.emergency_type = emergency_type
