from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):

    def __init__(self,
                 weight: int,
                 fuel: int,
                 fuel_consumption: float,
                ):

        self.started = False
        self.weight = weight    # self.weight = int(weight) ???
        self.fuel = fuel        # self.fuel = int(fuel)     ???
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance):
        fuel_for_trip = distance / 100 * self.fuel_consumption
        if fuel_for_trip > self.fuel:
            raise exceptions.NotEnoughFuel()
        else:
            self.fuel -= fuel_for_trip
