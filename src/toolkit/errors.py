import sys


def throw_error(error: str):
    sys.stderr.write("Error: " + str + "\n")
    sys.exit(2)


def throw_empty_expression():
    sys.stderr.write("The expression field is empty\n")
    sys.exit(2)


def throw_unexpected_symbol():
    sys.stderr.write("Expression contains unexpected symbols\n")
    sys.exit(2)


def throw_double_operands():
    sys.stderr.write("Expression contains two operators standing together\n")
    sys.exit(2)


def throw_missing_operand():
    sys.stderr.write("Missing operand in expression\n")
    sys.exit(2)


def throw_division_by_zero():
    sys.stderr.write("Expression contains division by zero\n")
    sys.exit(2)


def throw_unknown_unit():
    sys.stderr.write("Expression contains unknown units of measurement\n")
    sys.exit(2)


def throw_incompatible_units():
    sys.stderr.write("Can't convert this units\n")
    sys.exit(2)


def throw_wrong_value():
    sys.stderr.write("Wrong value has been entered\n")
    sys.exit(2)
