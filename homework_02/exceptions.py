#
# User defined exceptions
#


class LowFuelError(Exception):
    def __str__(self):
        return "## ERROR: ##   we have no fuel at all!"


class NotEnoughFuel(Exception):
    def __str__(self):
        return "## ERROR: ##   not enough fuel for a (such long) trip!"


class CargoOverload(Exception):
    def __str__(self):
        return "## ERROR: ##   overload detected - cargo is too heavy!"
