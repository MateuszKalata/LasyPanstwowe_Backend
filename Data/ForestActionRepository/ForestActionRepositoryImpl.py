import sqlalchemy.exc

from Data.ForestActionRepository.ForestActionMapper import ForestActionMapper
from Data.ForestActionRepository.IForestActionRepository import IForestActionRepository

from Entities.ForestActionEntity import ForestActionEntity
from Entities.ForestationTypeEntity import ForestationTypeEntity
from Utils.APIException import APIException
from Utils.DBhelper import Session


class ForestActionRepositoryImpl(IForestActionRepository):

    def __init__(self):
        self.forest_action_mapper = ForestActionMapper()

    def create(self, xforestaction):
        session = Session()
        forest_action_entity = self.forest_action_mapper.convert_XForestAction_to_ForestActionEntity(xforestaction)
        session.add(forest_action_entity)
        session.commit()
        forest_action_entity_id = forest_action_entity.id
        session.close()
        return forest_action_entity_id

    def read(self, id):
        session = Session()
        try:
            forest_action = session.query(ForestActionEntity).filter(ForestActionEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Forest Action with id={id} doesn't exist", 422)
        session.close()
        xforestaction = self.forest_action_mapper.convert_ForestActionEntity_to_XForestAction(forest_action)
        return xforestaction

    def read_all(self):
        session = Session()
        forest_actions = session.query(ForestActionEntity).all()
        session.close()
        xforestactions = map(self.forest_action_mapper.convert_ForestActionEntity_to_XForestAction, forest_actions)
        return xforestactions

    def update(self, id):
        session = Session()
        forest_action = session.query(ForestActionEntity).filter(ForestActionEntity.id == id).one()
        forestation_type = session.query(ForestationTypeEntity).filter(
            ForestationTypeEntity.forest_area_id == forest_action.forest_area_id,
            ForestationTypeEntity.name == forest_action.tree_type).one()
        if forest_action.type == 'forestation':
            session.query(ForestationTypeEntity).filter(
                ForestationTypeEntity.forest_area_id == forest_action.forest_area_id,
                ForestationTypeEntity.name == forest_action.tree_type).update(
                {"surface": int(forestation_type.surface) + forest_action.number_of_trees_to_proceed})
        else:
            session.query(ForestationTypeEntity).filter(
                ForestationTypeEntity.forest_area_id == forest_action.forest_area_id,
                ForestationTypeEntity.name == forest_action.tree_type).update(
                {"surface": int(forestation_type.surface) - forest_action.number_of_trees_to_proceed})
        session.query(ForestActionEntity).filter(ForestActionEntity.id == id).update({"status": 'finished'})
        session.commit()
        session.close()
        return 0
