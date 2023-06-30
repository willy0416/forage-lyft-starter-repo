import unittest

from tires.types.octoprime import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [0.65, 0.65, 0.85, 0.85]
        tires = OctoprimeTires(wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear = [0.89, 0.8, 0.7, 0.6]
        tires = OctoprimeTires(wear)
        self.assertFalse(tires.needs_service())
