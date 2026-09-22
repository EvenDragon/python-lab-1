from constants import NUMBERS, OPERATORS, LHOOK, RHOOK
import re

def checkPriority(a,b):
    """If op a's priority is higher or equal than op b return True"""
    return not((a==LHOOK) or (a==RHOOK)) and (OPERATORS.index(b) >= OPERATORS.index(a))

def tokenize( expr):

    # Removing horrible + and -
    expr = ' ' + expr
    expr = re.sub(r'([^0-9)])[+]', r'\1',expr)
    expr = re.sub(r'([^0-9])[-](\d(\.\d+)?)', r'\1(0-\2)',expr)


    postfix_expr = []
    operators = []
    is_float_now = False
    for i in expr:
        if i == ' ':
            continue

        if i == '.':
            is_float_now = True
            postfix_expr[-1] += '.'

        elif i in NUMBERS:
            if not is_float_now:
                postfix_expr += i
            else:
                postfix_expr[-1] += i

        else:
            if is_float_now:
                is_float_now = False

            if i in OPERATORS:
                while len(operators)>0 and checkPriority(operators[-1],i):
                    postfix_expr += operators.pop()
                operators.append(i)

            elif i == LHOOK:
                operators.append(i)

            elif i == RHOOK:
                while len(operators) > 0 and operators[-1] != LHOOK:
                    postfix_expr += operators.pop()
                if len(operators) == 0:
                    "Выкинуть ошибку"
                else:
                    operators.pop()

    while len(operators) > 0:
        if operators[-1] == LHOOK:
            "Выкинуть ошибку"
        postfix_expr += operators.pop()


    return postfix_expr