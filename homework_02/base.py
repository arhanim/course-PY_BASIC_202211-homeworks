#
# Base Classes definition
#


from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(
        self,
        weight: int = 1800,
        fuel: float = 63,
        fuel_consumption: float = 0.112,
    ):

        self.started = False
        self.weight = int(weight)
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance):
        fuel_for_trip = distance * self.fuel_consumption
        if fuel_for_trip > self.fuel:
            raise exceptions.NotEnoughFuel()
        else:
            self.fuel -= fuel_for_trip
