from abc import ABC, abstractmethod


class ISensorMeasurementReporting(ABC):

    @abstractmethod
    def report_measurement(self, measurement):
        pass
