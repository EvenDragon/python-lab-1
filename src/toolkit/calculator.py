from constants import OPERATORS

def addOp(a,b):
    return float(a)+float(b)
def subOp(a,b):
    return float(a)-float(b)
def multOp(a,b):
    return float(a)*float(b)
def divOp(a,b):
    return float(a)/float(b)

def calculate(expr: list):
    while len(expr)>1:
        for i in range(len(expr)):
            if str(expr[i]) in OPERATORS:
                a,b, op = expr[i-2], expr[i-1], expr[i]

                if op == '+':
                    expr[i] = addOp(a,b)
                elif op == '-':
                    expr[i] = subOp(a,b)
                elif op == '*':
                    expr[i] = multOp(a,b)
                elif op == '/':
                    expr[i] = divOp(a,b)

                expr = expr[:i-2] + expr[i:]
                break
    return expr[0]
