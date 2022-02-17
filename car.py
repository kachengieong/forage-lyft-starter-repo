from serviceable import Serviceable
from engines import Engine
from battery import Battery


class Car(Serviceable):
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()

    def needs_service(self):
        pass
