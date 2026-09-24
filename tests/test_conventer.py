import pytest
from toolkit import __main__

def test_converter_1():
    res = __main__._convert(36.6, 'c', 'f')
    assert abs(res - 97.88) < 10e-6

def test_converter_2():
    res = __main__._convert(100.0, 'f', 'c')
    assert abs(res - 37.7777777778) < 10e-6

def test_converter_3():
    res = __main__._convert(0.0, 'c', 'k')
    assert abs(res - 273.15) < 10e-6

def test_converter_4():
    res = __main__._convert(2500.0, 'g', 'kg')
    assert abs(res - 2.5) < 10e-6

def test_converter_5():
    res = __main__._convert(150.0, 'mm', 'cm')
    assert abs(res - 15.0) < 10e-6

def test_converter_6():
    res = __main__._convert(1.5, 'km', 'm')
    assert abs(res - 1500.0) < 10e-6

#Negative tests

@pytest.mark.xfail
def test_converter_unknown_from_unit():
    res = __main__._convert(10.0, 'xyz', 'c')
    assert res is None

@pytest.mark.xfail
def test_converter_unknown_unit():
    res = __main__._convert(10.0, 'c', 'xyz')
    assert res is None

@pytest.mark.xfail
def test_converter_incompatible_categories():
    res = __main__._convert(10.0, 'c', 'kg')
    assert res is None

@pytest.mark.xfail
def test_converter_length_to_temp():
    res = __main__._convert(100.0, 'm', 'f')
    assert res is None

@pytest.mark.xfail
def test_converter_wrong_value():
    res = __main__._convert("abc", 'c', 'f')
    assert res is None

@pytest.mark.xfail
def test_converter_below_absolute_zero():
    res = __main__._convert(-300.0, 'c', 'k')
    assert res is None