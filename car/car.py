from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable


class Car(Serviceable):
    """
    Base class for all Cars.
    """
    def __init__(self, eng: Engine, bat: Battery):
        self.engine: Engine = eng
        self.battery: Battery = bat

    def needs_service(self) -> bool:
        """
        Returns whether this car needs to be serviced.
        """
        return self.engine.needs_service() or self.battery.needs_service()
