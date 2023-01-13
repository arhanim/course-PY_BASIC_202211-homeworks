class LowFuelError(Exception):
    # def __init__(self):
    #     pass

    def __str__(self):
        return '##ERROR:  we have no fuel at all!'


class NotEnoughFuel(Exception):
    # def __init__(self):
    #     pass

    def __str__(self):
        return '##ERROR:  not enough fuel for (this long) trip.'


class CargoOverLoad(Exception):
    # def __init__(self):
    #     pass

    def __str__(self):
        return '##ERROR:  overload detected - cargo is too heavy.'
