from abc import ABC, abstractmethod
from Model.Core import SensorEntity

class IForestryRepository(ABC):

    @abstractmethod
    def create(self, SensorEntity):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def readAll(self):
        pass

    @abstractmethod
    def update(self, SensorEntity):
        pass