import enum

# Constansts for tokenization of expression, which will be calculated
NUMBERS = "0123456789"
OPERATORS = "*/+-"
LHOOK = "("
RHOOK = ")"

# Constansts for converter
LENGTH_UNITS = ["mm", "cm", "m", "km"]
MASS_UNITS = ["g", "kg"]
TEMP_UNITS = ["c", "f", "k"]

LENGTH_VALUES = [0.001, 0.01, 1, 1000]
MASS_VALUES = [1, 1000]
KELVIN_CELSIUS_DIFF = 273.15
CELSIUS_FAHRENHEIT_MULT = 1.8
CELSIUS_FAHRENHEIT_ADD = 32
FAHRENHEIT_ABSOLUTE_ZERO = -459.67


class TempUnits(enum.Enum):
    celsius = "c"
    fahrenheit = "f"
    kelvin = "k"
