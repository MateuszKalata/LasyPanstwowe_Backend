from abc import ABC, abstractmethod


class ISensorMeasurementRepository(ABC):

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_id(self, id):
        pass
