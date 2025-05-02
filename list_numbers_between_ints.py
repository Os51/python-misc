import math

def list_numbers(num1, num2):
    range_list = list(range(math.ceil(num1), math.floor(num2) + 1))
    print(range_list)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the end number: "))

find_range(num1, num2)