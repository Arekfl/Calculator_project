
import pytest
from calculator import Calculator

def test_sum():
    calc = Calculator(3, 2)
    assert calc.sum() == 5

def test_subtract():
    calc = Calculator(3, 2)
    assert calc.subtract() == 1

def test_multiply():
    calc = Calculator(3, 2)
    assert calc.multiply() == 6

def test_divide():
    calc = Calculator(6, 2)
    assert calc.divide() == 3

def test_divide_by_zero():
    calc = Calculator(6, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()

def test_negative_numbers():
    calc = Calculator(-4, -5)
    assert calc.sum() == -9
    assert calc.subtract() == 1
    assert calc.multiply() == 20
    assert calc.divide() == 0.8

def test_float_operations():
    calc = Calculator(5.5, 2.2)
    assert pytest.approx(calc.sum(), 0.01) == 7.7
    assert pytest.approx(calc.subtract(), 0.01) == 3.3
    assert pytest.approx(calc.multiply(), 0.01) == 12.1
    assert pytest.approx(calc.divide(), 0.01) == 2.5
