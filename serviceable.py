from abc import ABC, abstractmethod


class Serviceable(ABC):
    """
    Abstract class to be inherited by all cars.
    """
    @abstractmethod
    def needs_service(self) -> bool:
        pass
