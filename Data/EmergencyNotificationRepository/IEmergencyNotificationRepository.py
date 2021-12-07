from abc import ABC, abstractmethod

class IEmergencyNotificationRepository(ABC):

    @abstractmethod
    def create(self, emergency_notification_entity, db):
        pass

    @abstractmethod
    def read(self, id, db):
        pass

    @abstractmethod
    def readAll(self, db):
        pass

    @abstractmethod
    def update(self, emergency_notification_entity, db):
        pass