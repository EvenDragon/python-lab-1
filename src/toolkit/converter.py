import constants
from constants import LENGTH_UNITS, LENGTH_VALUES
from constants import MASS_UNITS, MASS_VALUES
from constants import TempUnits, CELSIUS_FAHRENHEIT_ADD, CELSIUS_FAHRENHEIT_MULT, KELVIN_CELSIUS_DIFF
import errors


def convert(value: float, unit1: str, unit2: str) -> float:
    """
    Convert "Value --from UNIT --to UNIT
    """
    if unit1 == unit2:
        return value

    if unit1 in LENGTH_UNITS and unit2 in LENGTH_UNITS:
        return (value * LENGTH_VALUES[LENGTH_UNITS.index(unit1)] /
                LENGTH_VALUES[LENGTH_UNITS.index(unit2)])

    elif unit1 in MASS_UNITS and unit2 in MASS_UNITS:
        return (value * MASS_VALUES[MASS_UNITS.index(unit1)] /
                MASS_VALUES[MASS_UNITS.index(unit2)])

    elif unit1 in TempUnits and unit2 in TempUnits:
        if unit1 == TempUnits.celsius.value and unit2 == TempUnits.kelvin.value:
            return value + KELVIN_CELSIUS_DIFF
        elif unit1 == TempUnits.kelvin.value and unit2 == TempUnits.celsius.value:
            return value - KELVIN_CELSIUS_DIFF

        if unit1 == TempUnits.celsius.value and unit2 == TempUnits.fahrenheit.value:
            return (value * CELSIUS_FAHRENHEIT_MULT) + CELSIUS_FAHRENHEIT_ADD
        elif unit1 == TempUnits.fahrenheit.value and unit2 == TempUnits.celsius.value:
            return (value - CELSIUS_FAHRENHEIT_ADD) / CELSIUS_FAHRENHEIT_MULT

        if unit1 == TempUnits.kelvin.value and unit2 == TempUnits.fahrenheit.value:
            return ((value - KELVIN_CELSIUS_DIFF) * CELSIUS_FAHRENHEIT_MULT) + CELSIUS_FAHRENHEIT_ADD
        elif unit1 == TempUnits.fahrenheit.value and unit2 == TempUnits.kelvin.value:
            return ((value) - CELSIUS_FAHRENHEIT_ADD) / CELSIUS_FAHRENHEIT_MULT + KELVIN_CELSIUS_DIFF

    else:
        errors.throw_error("Something gone wrong...")







