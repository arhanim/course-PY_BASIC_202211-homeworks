from homework_02 import base
from homework_02 import engine


class Plane(base.Vehicle):

    def __init__(self,
                 weight: int = 30000,
                 fuel: int = 2000,
                 fuel_consumption: float = 150,
                 max_cargo: int = 5000,
                 ):

        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
