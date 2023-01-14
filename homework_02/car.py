#
# Car subclass
#


from homework_02 import base
from homework_02 import engine


class Car(base.Vehicle):
    def __init__(
        self,
        weight: int = 1300,
        fuel: float = 46,
        fuel_consumption: float = 8.2,
        car_engine: engine.Engine = engine.Engine(1.6, 4),
    ):

        super().__init__(weight, fuel, fuel_consumption)
        self.engine = car_engine

    def set_engine(self, new_engine: engine.Engine):
        self.engine = new_engine
