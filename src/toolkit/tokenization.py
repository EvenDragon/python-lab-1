import re

from toolkit import errors
from toolkit.constants import LHOOK, NUMBERS, OPERATORS, RHOOK


def check_priority(a, b):
    """If op a's priority is higher or equal than op b return True"""
    return not ((a == LHOOK) or (a == RHOOK)) and (
        OPERATORS.index(b) >= OPERATORS.index(a)
    )


def tokenize_for_calculation(expr) -> list:
    """
    Tokenize entered expression and return list in postfix notation
    """
    # Removing unary + and -
    expr = " " + expr
    expr = re.sub(r"([^0-9)])[+]", r"\1", expr)
    expr = re.sub(r"([^0-9])[-](\d(\.\d+)?)", r"\1(0-\2)", expr)

    postfix_expr = []
    operators = []
    is_float_now = False

    # Shunting yard algorithm
    for index_i in range(len(expr)):
        i = expr[index_i]
        if i == " ":
            continue

        if i == ".":
            is_float_now = True
            postfix_expr[-1] += "."

        elif i in NUMBERS:
            if is_float_now or expr[index_i - 1] in NUMBERS:
                postfix_expr[-1] += i
            else:
                postfix_expr += i

        else:
            if is_float_now:
                is_float_now = False

            if i in OPERATORS:
                while len(operators) > 0 and check_priority(operators[-1], i):
                    postfix_expr += operators.pop()
                operators.append(i)

            elif i == LHOOK:
                operators.append(i)

            elif i == RHOOK:
                while len(operators) > 0 and operators[-1] != LHOOK:
                    postfix_expr += operators.pop()
                if len(operators) == 0:
                    errors.throw_missing_operand()
                else:
                    operators.pop()

    while len(operators) > 0:
        if operators[-1] == LHOOK:
            errors.throw_missing_operand()
        postfix_expr += operators.pop()

    return postfix_expr
