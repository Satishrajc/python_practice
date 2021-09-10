import time
import threading

start = time.perf_counter()

def do_something(sec):
	print(f" Sleep for {sec} sec")
	time.sleep(sec)

# ---------------------------------------------------------
# t1 = threading.Thread(target=do_something, args=[1])
# t2 = threading.Thread(target=do_something, args=[1])
# t1.start()
# t2.start()
#
# t1.join()
# t1.join()

# ---------------------------------------------------------

# Running thread in loop
threading_lit = []

for _ in range(5):
	t = threading.Thread(target=do_something, args=[2])
	t.start()
	threading_lit.append(t)

for thread in threading_lit:
	thread.join()

finish = time.perf_counter()
print(f"Took {round(finish - start)} to run")