from abc import ABC, abstractmethod


class Battery(ABC):
    """
    Abstract class to be inherited by all batteries.
    """

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if this battery is in need of service.
        """
        pass
