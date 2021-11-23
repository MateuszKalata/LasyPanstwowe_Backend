from abc import ABC, abstractmethod

class ISensorRepository(ABC):

    @abstractmethod
    def create(self, sensorEntity, db):
        pass

    @abstractmethod
    def read(self, id, db):
        pass

    @abstractmethod
    def readAll(self, db):
        pass

    @abstractmethod
    def update(self, SensorEntity, db):
        pass