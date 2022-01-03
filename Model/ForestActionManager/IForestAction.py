from abc import ABC, abstractmethod


class IForestAction(ABC):

    @abstractmethod
    def create_forest_action(self, xforestaction):
        pass

    @abstractmethod
    def get_forest_action(self, id):
        pass

    @abstractmethod
    def get_forest_actions(self):
        pass

    @abstractmethod
    def update_forest_action(self, id):
        pass
