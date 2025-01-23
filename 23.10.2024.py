
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)










class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b



def test_calculator_operations():
    calc = Calculator()

    assert calc.add(3, 2) == 5
    assert calc.subtract(5, 3) == 2

def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)









def add(a, b):
    return a + b

def subtract(a, b):
    return a - b





def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0




