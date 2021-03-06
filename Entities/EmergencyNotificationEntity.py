from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from conf import Base
from datetime import datetime


class EmergencyNotificationEntity(Base):
    __tablename__ = 'emergency_notifications'

    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    type = Column(Integer)
    timestamp = Column(String(200))

    sensor_id = Column(Integer, ForeignKey('sensor.id'))
    sensor = relationship("SensorEntity", back_populates="emergency_notifications")
    sensor_measurements = relationship("SensorMeasurementEntity", back_populates="emergency_notification")

    def __init__(self, id, status, sensor_id, type):
        self.id = id
        self.status = status
        self.sensor_id = sensor_id
        self.type = type
        self.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
