from engine.engine import Engine


class SternmanEngine(Engine):
    """
    A type of engine, evidently.
    """

    def __init__(self, light: bool):
        self.warning_light_on = light

    def needs_service(self) -> bool:
        """
        Determines if this engine is in need of service.
        """
        return self.warning_light_on
