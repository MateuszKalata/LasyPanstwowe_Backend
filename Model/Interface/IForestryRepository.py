from abc import ABC, abstractmethod

class IForestryRepository(ABC):

    @abstractmethod
    def create(self, forestryEntity):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def readAll(self):
        pass

