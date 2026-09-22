import pytest
from toolkit import main

def test_add():
    res = main.calc("29+6")
    assert res == 35