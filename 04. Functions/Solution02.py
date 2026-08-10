# Problem: Create a function that takes two numbers as parameters and returns their sum.
from Solution01 import get_positive_int

def sum(num1, num2):
    return num1+num2

def main():
    num_1 = get_positive_int("Enter first number to be added: ")
    num_2 = get_positive_int("Enter second number to be added: ")

    print(sum(num_1, num_2))

if __name__ == "__main__":
    main()