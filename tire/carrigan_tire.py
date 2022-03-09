from abc import ABC

from tires import Tire

class CarriganTire(Tire, ABC):
    def __init__(self, sensors):
        self.sensors = sensors
    def needs_service(self):
        for sensors_value in self.sensors:
            if sensors_value >= 0.9:
                return True
        return False
