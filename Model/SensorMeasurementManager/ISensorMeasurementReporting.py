from abc import ABC, abstractmethod


class ISensorMeasurementReporting(ABC):

    @abstractmethod
    def reportMeasurement(self, measurement):
        pass
