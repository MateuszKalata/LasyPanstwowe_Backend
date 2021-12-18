from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from conf import Base


class SensorMeasurementEntity(Base):
    __tablename__ = 'sensor_measurements'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer)
    timestamp = Column(String(200))
    value = Column(Integer)

    emergency_notification_id = Column(Integer, ForeignKey('emergency_notifications.id'))
    emergency_notification = relationship("EmergencyNotificationEntity", back_populates="sensor_measurements")

    def __init__(self, id, sensor_id, timestamp, value, emergency_notification_id=None):
        self.id = id
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.emergency_notification_id = emergency_notification_id

