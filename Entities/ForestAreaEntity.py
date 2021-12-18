from sqlalchemy import Column, Integer, String

from conf import Base


class ForestAreaEntity(Base):
    __tablename__ = 'forest_areas'

    id = Column(Integer, primary_key=True)
    forestry_id = Column(Integer)
    name = Column(String(200))
    surface = Column(String(200))

    def __init__(self, id, forestry_id, name, surface):
        self.id = id
        self.forestry_id = forestry_id
        self.name = name
        self.surface = surface
