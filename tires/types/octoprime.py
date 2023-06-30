from tires.tires import Tires
from typing import List


class OctoprimeTires(Tires):
    """
    A type of set of tires, evidently.
    """

    def __init__(self, wear_status: List[float]):
        self.wear = wear_status

    def needs_service(self) -> bool:
        """
        Determines if this engine is in need of service.
        """
        return sum(self.wear) >= 3
