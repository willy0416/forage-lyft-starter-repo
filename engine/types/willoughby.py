from engine.engine import Engine


class WilloughbyEngine(Engine):
    """
    A type of engine, evidently.
    """

    def __init__(self, before: int, now: int):
        self.last_service_mileage: int = before
        self.current_mileage: int = now

    def needs_service(self) -> bool:
        """
        Determines if this engine is in need of service.
        """
        return self.current_mileage - self.last_service_mileage >= 60000
