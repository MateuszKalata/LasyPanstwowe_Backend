from abc import ABC, abstractmethod


class IEmergencyNotificationRepository(ABC):

    @abstractmethod
    def create(self, x_emergency_notification):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, id, data):
        pass
