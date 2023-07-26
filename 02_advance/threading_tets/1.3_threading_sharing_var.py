import threading
import time

value = 0


def read_value():
    global value
    time.sleep(1)
    print("Read value is: ",  value)


def increment_value():
    global value
    print("Value before incrementing: ", value)
    value += 1


incr_thread = threading.Thread(target=increment_value)
read_thread = threading.Thread(target=read_value)
incr_thread.start()
read_thread.start()

incr_thread.join()
read_thread.join()
