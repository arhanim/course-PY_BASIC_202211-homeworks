#
# Engine dataclass
#


from dataclasses import dataclass


@dataclass
class Engine:
    volume: float
    pistons: int
