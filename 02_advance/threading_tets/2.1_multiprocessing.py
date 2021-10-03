import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()


def do_something(sec):
    # print(f" Sleep for {sec} sec")
    time.sleep(sec)
    return f"Waiting for {sec}"


if __name__ == '__main__':
    print(f" CPU count: {multiprocessing.cpu_count()}")

    # t1 = multiprocessing.Process(target=do_something, args= (1,))
    # t2 = multiprocessing.Process(target=do_something, args= (1,))
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

    # ------------------------------------------------------------------

    # processes = []
    # for _ in range(5):
    # 	t = multiprocessing.Process(target=do_something, args=(1,))
    # 	processes.append(t)
    # 	t.start()
    #
    # for prcoces in processes:
    # 	prcoces.join()

    # ------------------------------------------------------------------
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    # 	seconds = [1,4,5,2,3]
    #
    # 	f1 = executor.submit(do_something, 1)
    # 	f2 = executor.submit(do_something, 1)
    #
    # 	# Wait to complete the threading process
    # 	print(f1.result())
    # 	print(f2.result())
    # ------------------------------------------------------------------

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    # 	seconds = [1, 4, 5, 2, 3]
    #
    # 	f = [executor.submit(do_something, sec) for sec in seconds]
    #
    # 	# Wait to complete the threading process
    # 	for res in concurrent.futures.as_completed(f):
    # 		print(res.result())

    # ------------------------------------------------------------------

    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [1, 4, 5, 2, 3]
        f = executor.map(do_something, seconds)
        for res in f:
            print(res)

    finish = time.perf_counter()
    print(f"Took {round(finish - start)} to run")
