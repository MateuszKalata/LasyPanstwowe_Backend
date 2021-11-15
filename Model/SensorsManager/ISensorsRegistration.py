from abc import ABC, abstractmethod

class ISensorsRegistration(ABC):

    @abstractmethod
    def RegisterSensor(self, sensor):
        pass