from abc import ABC, abstractmethod

class ISensors(ABC):

    @abstractmethod
    def AssignSensor(self, sensorId, forestAreaId):
        pass

    @abstractmethod
    def GetSensor(self, id):
        pass

    @abstractmethod
    def GetSensorsByForestry(self, forestryId):
        pass

    @abstractmethod
    def GetSensorsNotAssigned(self):
        pass
