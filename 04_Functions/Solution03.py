# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
from Solution01 import get_positive_int

def multiply(data, n):
    try:
        data = float(data)
    except ValueError:
        n = int(n)
        pass

    return data*n


user_input = input("Enter something to multiply: ").strip()
by = get_positive_int("By how much you want to multiply with: ", is_float="Y")
print("answer:", multiply(user_input, by))