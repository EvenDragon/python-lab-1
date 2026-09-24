from toolkit import calculator
from toolkit import converter
from toolkit import tokenization
import typer
from toolkit import validation

app = typer.Typer()

def _calc(expression: str) -> str:
    """Local func that return result of all operations"""
    if validation.validate_calc(expression):
        tokenized_expr = tokenization.tokenize_for_calculation(expression)
        calculated_answer = calculator.calculate(tokenized_expr)
        return calculated_answer

def _convert(value: float, unit1: str, unit2: str):
    "Local func that return result of all operations"
    if validation.validate_convert(value, unit1, unit2):
        converted_answer = converter.convert(value, unit1, unit2)
        return converted_answer

@app.command(context_settings={"ignore_unknown_options": True})
def calc(expression: str) -> None:
    """Calculate "EXPRESSION"""
    print(_calc(expression))

@app.command(context_settings={"ignore_unknown_options": True})
def convert(value: float, unit1: str, unit2: str):
    """
    Convert "Value from UNIT to UNIT"
    Can convert lenth, mass, temp
    mm, cm, m, km
    g, kg
    c, f, k
    """
    print(_convert(value,unit1,unit2))


if __name__ == "__main__":
    app()
