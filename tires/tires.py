from abc import ABC, abstractmethod


class Tires(ABC):
    """
    Abstract class to be inherited by all engines.
    """

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if this engine is in need of service.
        """
        pass
