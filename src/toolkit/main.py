import argparse
import typer
import tokenization
import calculator

app = typer.Typer()

@app.command()
def calc(expression: str) -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    # parser = argparse.ArgumentParser()
    # parser.add_argument("calc",help="Calculates some EXPRESSION",type=str)
    # args = parser.parse_args()
    # expr = args.calc

    tokenized_expr = tokenization.tokenize(expression)
    print(tokenized_expr)
    calculated_answer = calculator.calculate(tokenized_expr)
    print(calculated_answer)

@app.command()
def convert():
    print("conv")



if __name__ == "__main__":
    app()
