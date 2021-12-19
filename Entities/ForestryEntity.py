from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from conf import Base


class ForestryEntity(Base):
    __tablename__ = 'forestries'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    surface = Column(String(200))

    forest_areas = relationship("ForestAreaEntity", back_populates="forestry")

    def __init__(self, id, name, surface):
        self.id = id
        self.name = name
        self.surface = surface
