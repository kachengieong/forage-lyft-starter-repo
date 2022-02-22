from abc import ABC

from serviceable import Serviceable

from engines import Engine
from batterys import Battery

class Car(Serviceable, ABC):
    def __init__(self, engine:Engine, battery:Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
