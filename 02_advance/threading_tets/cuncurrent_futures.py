# https://www.youtube.com/watch?v=IEEhzQoKtQU&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=124

import concurrent.futures
import time

start = time.perf_counter()


def do_something(sec):
    # print(f" Sleep for {sec} sec")
    time.sleep(sec)
    return f"slpet for {sec}"


# ---------------------------------------------------------
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)

    # Wait to complete the threading process
    print(f1.result())
    print(f2.result())

# ---------------------------------------------------------

# Running thread in loop
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [1, 2, 3, 4, 1]
    f = [executor.submit(do_something, sec) for sec in seconds]

    for res in concurrent.futures.as_completed(f):
        print(res.result())

finish = time.perf_counter()
print(f"Took {round(finish - start)} to run")
# ---------------------------------------------------------

# Running thread in loop with map function
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [1, 2, 3, 4, 1]
    f = executor.map(do_something, seconds)

    for res in f:
        print(res)

finish = time.perf_counter()
print(f"Took {round(finish - start)} to run")
