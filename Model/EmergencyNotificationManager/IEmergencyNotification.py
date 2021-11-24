from abc import ABC, abstractmethod


class IEmergencyNotification(ABC):

    @abstractmethod
    def get_emergency_notification(self, id):
        pass

    @abstractmethod
    def get_emergency_notifications(self):
        pass

    @abstractmethod
    def mark_emergency_as_resolved(self, id):
        pass
