from abc import ABC

from engines import Engine


class WilloughbyEngine(Engine, ABC):
    def __init__(self,current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
