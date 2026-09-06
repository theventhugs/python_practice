# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time

def cached(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cached
def example_function(x, y):
    time.sleep(1)
    return x+y


print(example_function(4, 5))
print(example_function(4, 5))
print(example_function(1, 2))