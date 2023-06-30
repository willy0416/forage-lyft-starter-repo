import unittest
from datetime import date

from battery.types.spindler import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2019-05-15")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2008-11-27")
        last_service_date = date.fromisoformat("2007-04-16")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
