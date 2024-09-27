from abc import ABC, abstractmethod

class ITransaction(ABC):
    @abstractmethod
    def execute(self):
        pass
