import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.ForestryRepository.ForestryMapper import ForestryMapper
from Data.ForestryRepository.IForestryRepository import IForestryRepository
from Entities.ForestryEntity import ForestryEntity
from conf import DB_URI


class ForestryRepositoryImpl(IForestryRepository):

    def __init__(self):
        self.forestry_mapper = ForestryMapper()
        self.engine = create_engine(DB_URI)
        self.Session = sessionmaker(bind=self.engine)
        ForestryEntity.metadata.create_all(bind=self.engine)

    def create(self, xforestry):
        session = self.Session()
        forestry_entity = self.forestry_mapper.convert_xforestry_to_forestry_entity(xforestry)
        session.add(forestry_entity)
        session.commit()
        session.close()
        return 0

    def read(self, id):
        session = self.Session()
        try:
            forestry_entity = session.query(ForestryEntity).filter(ForestryEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xforestry = self.forestry_mapper.convert_forestry_entity_to_xforestry(forestry_entity)
        return xforestry

    def read_all(self):
        session = self.Session()
        forestry_entities = session.query(ForestryEntity).all()
        session.close()
        xforestries = map(self.forestry_mapper.convert_forestry_entity_to_xforestry, forestry_entities)
        return xforestries
