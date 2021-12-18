from sqlalchemy import Column, Integer, String

from conf import Base


class ForestationTypeEntity(Base):
    __tablename__ = 'forestation_types'

    id = Column(Integer, primary_key=True)
    forest_area_id = Column(Integer)
    name = Column(String(200))
    surface = Column(String(200))

    def __init__(self, id, forest_area_id, name, surface):
        self.id = id
        self.forest_area_id = forest_area_id
        self.name = name
        self.surface = surface
