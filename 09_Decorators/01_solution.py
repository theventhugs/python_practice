# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  func(*args, **kwargs)
        stop = time.time()

        print(f"{func.__name__} ran for {stop-start:.2f} seconds")
        return result
    return wrapper

@timer #with this, example_func will only be called after calling timer function
def example_func(n):
    time.sleep(n)


# calling the function
example_func(2)