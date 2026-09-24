import pytest
from toolkit import __main__

def test_calc1():
    res = __main__._calc("29+6")
    assert res == 35

def test_calc2():
    res = __main__._calc(" 10-4")
    assert res == 6

def test_calc3():
    res = __main__._calc("7*8")
    assert res == 56

def test_calc4():
    res = __main__._calc("20/5")
    assert res == 4

def test_calc5():
    res = __main__._calc("2+3*4")
    assert res == 14

def test_calc6():
    res = __main__._calc("(2+3)*4")
    assert res == 20

def test_calc7():
    res = __main__._calc("---5+10")
    assert res == 5

# Negative tests

@pytest.mark.xfail
def test_calc_empty_expression():
    res = __main__._calc("")
    assert res is None

@pytest.mark.xfail
def test_calc_unknown_character():
    res = __main__._calc("2+abc")
    assert res is None

@pytest.mark.xfail
def test_calc_missing_operand():
    res = __main__._calc("5+")
    assert res is None

@pytest.mark.xfail
def test_calc_two_operators():
    res = __main__._calc("3+*4")
    assert res is None

@pytest.mark.xfail
def test_calc_division_by_zero():
    res = __main__._calc("10/0")
    assert res is None