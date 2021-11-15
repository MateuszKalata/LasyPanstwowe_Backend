from abc import ABC, abstractmethod


class IForestries(ABC):

    @abstractmethod
    def create_forestry(self, forestry):
        pass

    @abstractmethod
    def get_forestry(self, id):
        pass

    @abstractmethod
    def get_forestries(self):
        pass
