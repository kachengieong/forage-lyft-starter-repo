import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class testCarrigan(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        sensors = [0.8, 0.9, 0.95, 0.5]
        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())
    def test_carrigan_should_not_be_serviced(self):
        sensors = [0.7, 0.3, 0.53, 0.64]
        tire = CarriganTire(sensors)
        self.assertFalse(tire.needs_service())

class testOctoprime(unittest.TestCase):
    def test_octoprime_should_be_serviced(self):
        sensors = [0.9, 0.95, 0.5, 0.7]
        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service())
    def test_octoprime_should_not_be_serviced(self):
        sensors = [0.5, 0.4, 0.64, 0.85]
        tire = OctoprimeTire(sensors)
        self.assertFalse(tire.needs_service())