from battery.battery import Battery
from datetime import date, datetime


class NubbinBattery(Battery):
    """
    A type of car battery, evidently.
    """

    def __init__(self, before: date, now: date):
        self.last_service_date: date = before
        self.current_date: date = now

    def needs_service(self) -> bool:
        """
        Determines if this battery is in need of service.
        """
        # self.current_date = datetime.now()
        last_viable_date: int = self.last_service_date.toordinal() + (365 * 4)
        return self.current_date.toordinal() >= last_viable_date
