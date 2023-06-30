import unittest
from datetime import date

from battery.types.nubbin import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-09-13")
        last_service_date = date.fromisoformat("2017-11-09")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2019-06-11")
        last_service_date = date.fromisoformat("2019-05-19")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
