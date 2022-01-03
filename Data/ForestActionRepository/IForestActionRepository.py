from abc import ABC, abstractmethod


class IForestActionRepository(ABC):

    @abstractmethod
    def create(self, XForestAction):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, id):
        pass
