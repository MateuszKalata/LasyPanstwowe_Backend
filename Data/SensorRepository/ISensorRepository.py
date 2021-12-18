from abc import ABC, abstractmethod


class ISensorRepository(ABC):

    @abstractmethod
    def create(self, sensorEntity):
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
