from app import calculate

def test_add():
    assert calculate(2, 3, "Add") == 5

def test_subtract():
    assert calculate(10, 4, "Subtract") == 6

def test_multiply():
    assert calculate(3, 5, "Multiply") == 15

def test_divide():
    assert calculate(10, 2, "Divide") == 5

def test_divide_by_zero():
    assert calculate(10, 0, "Divide") == "❌ Error: Division by zero"