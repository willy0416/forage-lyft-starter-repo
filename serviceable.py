from abc import ABC, abstractmethod


class Serviceable(ABC):
    """
    Abstract class to be inherited by all car.
    """

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if this vehicle is in need of service.
        """
        pass
