from numba import jit

import concurrent.futures
from time import perf_counter

start = perf_counter()

@jit(nopython=True, parallel=True)
def foo(r):
	for i in range(r):
		rec = i*i*i*i*i*i*i*i*i*i*i*i
		rec1 = i*i*i*i*i*i*i*i*i*i*i*i
		rec2 = i*i*i*i*i*i*i*i*i*i*i
	return


if __name__ == '__main__':
	R = range(1000)
	# with concurrent.futures.ProcessPoolExecutor() as executor:
	# 	# p = executor.submit(foo)
	# 	p = executor.map(foo, R)

	# with concurrent.futures.ThreadPoolExecutor() as executor:
	# 	# p = executor.submit(foo)
	# 	p = executor.map(foo, R)

	for i in R:
		foo(i)
	print(f"Finished: {round(perf_counter() - start, 2)}")
