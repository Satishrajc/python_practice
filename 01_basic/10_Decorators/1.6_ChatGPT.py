# Write a Python decorator called timing_decorator that measures the execution 
# time of a function and prints the time taken for it to run. The decorator should 
# work with functions that have any number of arguments.



import time

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        print(*args)
        result = func(*args, **kwargs)
        
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__}{args} took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper

# Test the timing_decorator with a sample function
@timing_decorator
def calculate_power(base, exponent):
    return base ** exponent

# Test the decorated function
calculate_power(2, 5)


@timing_decorator
def calculate_power(base, exponent):
    return base ** exponent


calculate_power(10,1000000000)


# Note: If you don't provide any arguments when calling a function that uses *args and/or 
# **kwargs, it will still work without any issues. When you don't pass any arguments, 
# the *args and **kwargs will simply be empty (an empty tuple for *args and an empty 
# dictionary for **kwargs).