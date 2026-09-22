from toolkit import calculator
from toolkit import converter
from toolkit import tokenization
import typer
from toolkit import validation

app = typer.Typer()


@app.command(context_settings={"ignore_unknown_options": True})
def calc(expression: str) -> None:
    """
    Calculate "EXPRESSION"
    """

    if validation.validate_calc(expression):
        tokenized_expr = tokenization.tokenize_for_calculation(expression)
        calculated_answer = calculator.calculate(tokenized_expr)
        print(calculated_answer)


@app.command(context_settings={"ignore_unknown_options": True})
def convert(value: float, unit1: str, unit2: str):
    """
    Convert "Value from UNIT to UNIT"
    Can convert lenth, mass, temp
    """
    if validation.validate_convert(value, unit1, unit2):
        converted_answer = converter.convert(value, unit1, unit2)
        print(converted_answer)


if __name__ == "__main__":
    app()
