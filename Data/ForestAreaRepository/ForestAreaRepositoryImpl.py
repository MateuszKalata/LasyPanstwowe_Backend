import sqlalchemy.exc

from Data.ForestAreaRepository.ForestAreaMapper import ForestAreaMapper
from Data.ForestAreaRepository.IForestAreaRepository import IForestAreaRepository
from Entities.ForestAreaEntity import ForestAreaEntity
from Entities.ForestationTypeEntity import ForestationTypeEntity
from Utils.DBhelper import Session


class ForestAreaRepositoryImpl(IForestAreaRepository):

    def __init__(self):
        self.forest_area_mapper = ForestAreaMapper()

    def create(self, xforestarea):
        session = Session()
        forest_area_entity = self.forest_area_mapper.convert_xforestarea_to_forest_area_entity(xforestarea)
        session.add(forest_area_entity)
        session.commit()
        forest_area_id = forest_area_entity.id
        [
            session.add(
                ForestationTypeEntity(
                    None,
                    forest_area_id,
                    ft['name'],
                    ft['surface']
                )) for ft in xforestarea.forestation_types
        ]
        session.commit()
        session.close()
        return forest_area_id

    def read(self, id):
        session = Session()
        try:
            forest_area_entity = session.query(ForestAreaEntity).filter(ForestAreaEntity.id == id).one()
            forestation_types = session.query(ForestationTypeEntity) \
                .filter(ForestationTypeEntity.forest_area_id == forest_area_entity.id).all()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xforestarea = self.forest_area_mapper.convert_forest_area_entity_to_xforestarea(forest_area_entity)
        xforestarea.forestation_types = [{"name": ft.name, "surface": ft.surface} for ft in forestation_types]
        return xforestarea

    def read_all(self):
        session = Session()
        forestry_entities = session.query(ForestAreaEntity).all()
        xforestareas = list(map(self.forest_area_mapper.convert_forest_area_entity_to_xforestarea, forestry_entities))
        for i in range(0, len(xforestareas)):
            forestation_types = session.query(ForestationTypeEntity) \
                .filter(ForestationTypeEntity.forest_area_id == xforestareas[i].id).all()
            xforestareas[i].forestation_types = [{"name": ft.name, "surface": ft.surface} for ft in forestation_types]
        session.close()
        return xforestareas
