import re
import errors
from constants import LENGTH_UNITS, MASS_UNITS, TEMP_UNITS, TempUnits, FAHRENHEIT_ABSOLUTE_ZERO
from constants import CELSIUS_FAHRENHEIT_ADD


def validate_calc(expr: str) -> bool:
    """
    Return True if no errors detected, in other cases return False
    """
    double_ops = r'[+/*-]\s*[+/*-]'
    unexpected_symbols = r'[^0-9\s/*+.-]'
    expr = expr.strip()
    if len(expr) == 0:
        errors.throw_empty_expression()

    elif len(re.findall(double_ops,expr)):
        errors.throw_double_operands()

    elif len(re.findall(unexpected_symbols,expr)):
        errors.throw_unexpected_symbol()



    else:
        return True

    return False

def validate_convert(value: float, unit1: str, unit2: str) -> bool:
    """
    Return True if no errors detected, in other cases return False
    """
    if unit1 in LENGTH_UNITS and unit2 in LENGTH_UNITS:
        if value < 0:
            errors.throw_wrong_value()
            return False
        else:
            return True

    elif unit1 in MASS_UNITS and unit2 in MASS_UNITS:
        if value < 0:
            errors.throw_wrong_value()
            return False
        else:
            return True

    elif unit1 in TempUnits and unit2 in TempUnits:
        if (unit1 == TempUnits.celsius.value and value < -CELSIUS_FAHRENHEIT_ADD) \
                or (unit1 == TempUnits.kelvin.value and value < 0) \
                or (unit1 == TempUnits.fahrenheit.value and value < FAHRENHEIT_ABSOLUTE_ZERO):
            errors.throw_wrong_value()
            return False
        else:
            return True

    else:
        errors.throw_unknown_unit()
        return False