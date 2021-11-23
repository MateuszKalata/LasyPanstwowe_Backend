from abc import ABC, abstractmethod


class ISensorMeasurements(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_measurements_by_sensor_id(self, sensor_id):
        pass
