from abc import ABC, abstractmethod


class IForestAreas(ABC):

    @abstractmethod
    def create_forest_area(self, forest_area):
        pass

    @abstractmethod
    def get_forest_areas(self, forestry_id):
        pass
