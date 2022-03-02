from math_series.math_series import fibonacci, lucas, sum_series


"""
Fibonacci Series:
    n: 0, 1, 2, 5, 20, -10, 5.5, -2.2 , 2**2, "Not an Integer"

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1
        return fibonacci(n - 1) + fibonacci(n - 2)
"""

# Test Cases for fibonacci function:

# Test the first two numbers in the series
def test_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

# Test any positive integer
def test_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_four():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_five():
    actual = fibonacci(20)
    expected = 6765
    assert actual == expected

# Test negative integer
def test_six():
    actual = fibonacci(-10)
    expected = -1
    assert actual == expected

# Test float number
def test_fibonacci():
    actual = fibonacci(5.5)
    expected = TypeError
    assert actual == expected

# Test negative float number
def test_fibonacci():
    actual = fibonacci(-2.2)
    expected = TypeError
    assert actual == expected

# Array of numbers
def test_fibonacci():
    actual = fibonacci([1,2,3,4])
    expected = TypeError
    assert actual == expected

# List of numbers
def test_fibonacci():
    actual = fibonacci({"1":1, "2":2, "3":3})
    expected = TypeError
    assert actual == expected

# Exponents
def test_seven():
    actual = fibonacci(2**2)
    expected = 3
    assert actual == expected

def test_fibonacci_type_error():
    actual = sum_series("Not an Integer")
    expected = TypeError
    assert actual == expected


# Test Cases for lucas function:

# Test the first two numbers in the series
def test_first():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_second():
    actual = lucas(1)
    expected = 1
    assert actual == expected

# Test any positive integer
def test_third():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_fourth():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_fifth():
    actual = lucas(20)
    expected = 15127
    assert actual == expected

# Test negative integer
def test_sixth():
    actual = lucas(-10)
    expected = -1
    assert actual == expected

# Test float number
def test_lucas():
    actual = lucas(5.5)
    expected = TypeError
    assert actual == expected

# Test negative float number
def test_lucas():
    actual = lucas(-2.2)
    expected = TypeError
    assert actual == expected

# Array of numbers
def test_lucas():
    actual = lucas([1,2,3,4])
    expected = TypeError
    assert actual == expected
# List of numbers
def test_lucas():
    actual = lucas({"1":1, "2":2, "3":3})
    expected = TypeError
    assert actual == expected

# Exponents
def test_seventh():
    actual = lucas(2**2)
    expected = 7
    assert actual == expected

def test_lucas_type_error():
    actual = sum_series("Not an Integer")
    expected = TypeError
    assert actual == expected


# Test Cases for sum_series function:

def test_sum01():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum02():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum03():
    actual = sum_series(5, 2, 1)
    expected = 5
    assert actual == expected

def test_type_error():
    actual = sum_series("Not an Integer")
    expected = TypeError
    assert actual == expected