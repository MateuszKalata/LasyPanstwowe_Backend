from abc import ABC, abstractmethod


class IEmergencyReporting(ABC):

    @abstractmethod
    def report_emergency(self, x_emergency_notification):
        pass
