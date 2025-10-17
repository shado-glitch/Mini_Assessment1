def product(num1, num2):
    
    product = num1*num2
    return product
    pass


def square(number):
    
    square = (number)**2
    return square
    pass


def even(n):
    
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
    number_list = list(numbers)

    odd_numbers = []
    for i in number_list:
        if i % 2 != 0:
            odd_numbers.append(i)
    print(odd_numbers)  
    return sum(odd_numbers)

    pass
