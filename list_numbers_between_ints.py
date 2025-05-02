import math

def list_numbers(num1, num2):
    return list(range(math.ceil(num1), math.floor(num2) + 1))


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the end number: "))

print(list_numbers(num1, num2))