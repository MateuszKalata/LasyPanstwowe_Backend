from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class SensorMeasurementEntity(Base):
    __tablename__ = 'sensor_measurements'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer)
    sensor_name = Column(String(200))
    value = Column(Integer)
    unit = Column(String(200))
    date = Column(String(200))
    is_critical = Column(Boolean)

    def __init__(self, id, sensor_id, sensor_name, value, unit, date, is_critical):
        self.id = id
        self.sensor_id = sensor_id
        self.sensor_name = sensor_name
        self.value = value
        self.unit = unit
        self.date = date
        self.is_critical = is_critical
