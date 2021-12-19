from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from conf import Base


class ForestAreaEntity(Base):
    __tablename__ = 'forest_areas'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    surface = Column(String(200))

    forestry_id = Column(Integer, ForeignKey('forestries.id'))
    forestry = relationship("ForestryEntity", back_populates="forest_areas")
    sensors = relationship("SensorEntity", back_populates="forest_area")

    def __init__(self, id, forestry_id, name, surface):
        self.id = id
        self.forestry_id = forestry_id
        self.name = name
        self.surface = surface
