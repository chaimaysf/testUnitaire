# test_rpn_calculator.py
import pytest
from rpn_calculator import RPNCalculator

def test_single_number():
    calc = RPNCalculator()
    assert calc.evaluate("5") == 5

def test_addition():
    calc = RPNCalculator()
    assert calc.evaluate("3 4 +") == 7
def test_subtraction():
    calc = RPNCalculator()
    assert calc.evaluate("10 4 -") == 6
def test_multiplication():
    calc = RPNCalculator()
    assert calc.evaluate("3 4 *") == 12