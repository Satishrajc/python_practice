# Implement a context manager in Python that measures the execution time of a code block 
# and prints the time taken
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"Execution time: {execution_time:.4f} seconds")

# Test the Timer context manager
with Timer():
    for _ in range(1000000):
        ...
