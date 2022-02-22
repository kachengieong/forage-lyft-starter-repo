from abc import ABC

from serviceable import Serviceable

from engines import Engine
from battery import Battery

class Car(Serviceable, ABC):
    def __init__(self, engine:Engine, battery:Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        self.engine.needs_service()
        self.battery.needs_service()
