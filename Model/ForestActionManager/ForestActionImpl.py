from DTO.XForestAction import XForestAction
from Data.ForestActionRepository.ForestActionRepositoryImpl import ForestActionRepositoryImpl
from Model.ForestActionManager.IForestAction import IForestAction


class ForestActionImpl(IForestAction):

    def __init__(self):
        self.forest_action_repository = ForestActionRepositoryImpl()

    def create_forest_action(self, xforestaction):
        return self.forest_action_repository.create(xforestaction)

    def get_forest_action(self, id):
        return self.forest_action_repository.read(id)

    def get_forest_actions(self):
        return self.forest_action_repository.read_all()

    def update_forest_action(self, id):
        return self.forest_action_repository.update(id)
