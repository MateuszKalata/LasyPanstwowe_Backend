from abc import ABC, abstractmethod


class IForestryRepository(ABC):

    @abstractmethod
    def create(self, forestry_entity):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def read_all(self):
        pass
