from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class SensorMeasurementEntity(Base):
    __tablename__ = 'sensor_measurements'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer)
    timestamp = Column(String(200))
    value = Column(Integer)

    def __init__(self, id, sensor_id, timestamp, value):
        self.id = id
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
