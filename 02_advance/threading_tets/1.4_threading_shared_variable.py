import threading

shared_variable = 0
shared_lock = threading.Lock()

def increment_shared_variable():
    global shared_variable
    for _ in range(1000000):
        # Acquire the lock before accessing the shared variable
        shared_lock.acquire()
        shared_variable += 1
        # Release the lock after modifying the shared variable
        shared_lock.release()

def decrement_shared_variable():
    global shared_variable
    for _ in range(1000000):
        # Acquire the lock before accessing the shared variable
        shared_lock.acquire()
        shared_variable -= 1
        # Release the lock after modifying the shared variable
        shared_lock.release()

# Create two threads to increment and decrement the shared variable concurrently
thread1 = threading.Thread(target=increment_shared_variable)
thread2 = threading.Thread(target=decrement_shared_variable)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final value of shared_variable:", shared_variable)
