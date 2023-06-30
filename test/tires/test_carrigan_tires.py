import unittest

from tires.types.carrigan import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [0.9, 0.8, 0.7, 0.6]
        tires = CarriganTires(wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear = [0.89, 0.8, 0.7, 0.6]
        tires = CarriganTires(wear)
        self.assertFalse(tires.needs_service())
