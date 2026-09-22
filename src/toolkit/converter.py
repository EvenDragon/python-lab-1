import constants
from constants import LENGTH_UNITS, LENGTH_VALUES


def convert(value: float, unit1: str, unit2: str) -> float:
    """
    Convert "Value --from UNIT --to UNIT
    """
    if unit1 == unit2:
        return value

    if unit1 in LENGTH_UNITS and unit2 in LENGTH_UNITS:
        return (value * LENGTH_VALUES[LENGTH_UNITS.index(unit1)] /
                LENGTH_VALUES[LENGTH_UNITS.index(unit2)])


