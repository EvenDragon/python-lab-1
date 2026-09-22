from constants import OPERATORS

def add_op(a, b):
    return float(a)+float(b)
def sub_op(a, b):
    return float(a)-float(b)
def mult_op(a, b):
    return float(a)*float(b)
def div_op(a, b):
    return float(a)/float(b)

def calculate(expr: list):
    while len(expr)>1:
        for i in range(len(expr)):
            if str(expr[i]) in OPERATORS:

                a,b, op = expr[i-2], expr[i-1], expr[i]

                if op == '+':
                    expr[i] = add_op(a, b)
                elif op == '-':
                    expr[i] = sub_op(a, b)
                elif op == '*':
                    expr[i] = mult_op(a, b)
                elif op == '/':
                    expr[i] = div_op(a, b)

                expr = expr[:i-2] + expr[i:]
                break
    return expr[0]
