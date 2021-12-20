from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class SensorEntity(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True)
    administrator = Column(String(200))
    dateAdded = Column(String(200))
    forestAreaId = Column(String(200))
    name = Column(String(200))
    status = Column(String(200))
    type = Column(String(200))
    unit = Column(String(200))
    longitude = Column(Float(8))
    latitude = Column(Float(8))


    def __init__(self,administrator,dateAdded, forestAreaId, name, status, type, unit, longitude, latitude):
        self.administrator = administrator
        self.dateAdded = dateAdded
        self.forestAreaId = forestAreaId
        self.name = name
        self.status = status
        self.type = type
        self.unit = unit
        self.longitude = longitude
        self.latitude = latitude
