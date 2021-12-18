import sqlalchemy.exc

from Data.ForestryRepository.ForestryMapper import ForestryMapper
from Data.ForestryRepository.IForestryRepository import IForestryRepository
from Entities.ForestryEntity import ForestryEntity
from Utils.APIException import APIException
from db_helper import Session


class ForestryRepositoryImpl(IForestryRepository):

    def __init__(self):
        self.forestry_mapper = ForestryMapper()

    def create(self, xforestry):
        session = Session()
        forestry_entity = self.forestry_mapper.convert_xforestry_to_forestry_entity(xforestry)
        session.add(forestry_entity)
        session.commit()
        forestry_entity_id = forestry_entity.id
        session.close()
        return forestry_entity_id

    def read(self, id):
        session = Session()
        try:
            forestry_entity = session.query(ForestryEntity).filter(ForestryEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Forestry with id={id} doesn't exist", 422)
        session.close()
        xforestry = self.forestry_mapper.convert_forestry_entity_to_xforestry(forestry_entity)
        return xforestry

    def read_all(self):
        session = Session()
        forestry_entities = session.query(ForestryEntity).all()
        session.close()
        xforestries = map(self.forestry_mapper.convert_forestry_entity_to_xforestry, forestry_entities)
        return xforestries
