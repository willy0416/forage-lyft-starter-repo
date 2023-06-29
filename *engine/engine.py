from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Abstract class to be inherited by all engines.
    """
    @abstractmethod
    def needs_service(self) -> bool:
        pass
