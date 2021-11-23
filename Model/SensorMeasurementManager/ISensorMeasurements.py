from abc import ABC, abstractmethod


class ISensorMeasurements(ABC):

    @abstractmethod
    def getAllMeasurements(self):
        pass

    @abstractmethod
    def getMeasurementsBySensorId(self, sensor_id):
        pass
