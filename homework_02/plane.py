from homework_02 import base
from homework_02 import exceptions


class Plane(base.Vehicle):

    def __init__(self,
                 weight: int = 30000,
                 fuel: float = 2000,
                 fuel_consumption: float = 1.5,
                 max_cargo: int = 5000,
                 ):

        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_weight):
        if (self.cargo + cargo_weight) > self.max_cargo:
            raise exceptions.CargoOverload()
        else:
            self.cargo += cargo_weight

    def remove_all_cargo(self) -> int:
        weight_removed = self.cargo
        self.cargo = 0
        return(weight_removed)
