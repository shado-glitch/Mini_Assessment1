def product(num1, num2):
    
    product = num1*num2
    return product
    pass


def square(number):
    """
    Returns the square of a number.

    Parameters:
        number (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    pass


def even(n):
    """
    Checks whether a number is even.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if n is even, False otherwise.
    """
    if n % 2 == 0 :
        return True
    else:
        return False
    pass


def sum_of_list(numbers):
    sum_of_list=sum(numbers)
    return sum_of_list
    pass


def list_of_even_numbers(numbers):
    
    numbers_list = []
    even_numbers = []
    for i in range(numbers):
        numbers_list.append(i)
    for i in numbers_list[1:]:
        if i % 2 == 0:
            even_numbers.append(i)

    
    return even_numbers

    pass


def sum_of_odd_numbers(numbers):
    """
    Calculates the sum of all odd numbers in a list.

    Parameters:
        numbers (list of int): A list of integers.

    Returns:
        int: The sum of all odd numbers in the list.
    """
    pass


print(list_of_even_numbers(20))