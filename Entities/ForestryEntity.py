from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class ForestryEntity(Base):
    __tablename__ = 'forestries'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    surface = Column(String(200))

    def __init__(self, id, name, surface):
        self.id = id
        self.name = name
        self.surface = surface
