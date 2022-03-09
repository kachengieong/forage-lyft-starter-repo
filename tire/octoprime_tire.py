from abc import ABC

from tires import Tire

class OctoprimeTire(Tire, ABC):
    def __init__(self, sensors):
        self.sensors = sensors
    def needs_service(self):
        sum = 0.0
        for sensor_value in self.sensors:
            sum += sensor_value
        if sum >= 3:
            return True
        else:
            return False