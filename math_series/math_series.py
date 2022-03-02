# Fibonacci Series
def fibonacci(n):
    """
    A function that takes a number and returns is value by summing the previous two numbers. 

    The series start number is equal to 0, and the second number is equal to 1.

    Input: Integer

    Output: Returns the nth value in the fibonacci

    """
    try:
        if n < 0:
            return -1
        elif n == 0 or n == 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except:
        print("TypeError: The input should be an integer")

# Lucas Numbers 
def lucas(n): 
    """
    A function that takes a number and returns is value by summing the previous two numbers. 

    The series start number is equal to 2, and the second number is equal to 1.

    Input: Integer

    Output: Returns the nth value in the lucas

    """
    try:
        if n < 0:
            return -1
        elif n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return lucas(n - 1) + lucas(n - 2)
    except:
        print("TypeError: The input should be an integer")

# Sum Series
def sum_series(n, start_num = 0, second_num = 1):
    """
    A function that takes a number and returns is value by summing the previous two numbers. 

    The series takes a default arguments of 0,1 for the start and second numbers -> Febonacci
    If we passed te arguments 2,1, for the start and second numbers -> Lucas

    Input: Number (Positive Integer, Negative Integer, Positive Float, Negative Float, Exponents)

    Output: Returns the nth value in the lucas or fibonacci
    """
    try:
        if n < 0:
            return -1
        elif n == 0:
            return start_num
        elif n == 1:
            return second_num
        else:
            return sum_series(n - 1, start_num, second_num) + sum_series(n - 2, start_num, second_num)
    except:
        print("TypeError: The input should be an integer")