# thread : a flow of execution.like a separate order of instructions
# However each thread takes a turn running to achieve concurrency
# GLI = (Global interpreter lock)
# allows only one thread to take control of the lock

# cpu bound processes: process/tasks which spend most of its time waiting for internal events (cup intensive) use multiprocessing

# io bound: tasks/ jobs spend most of its' time waiting for external events (user input, web scrapping) use multithreading

import threading
import time


def eatBreakFast():
    time.sleep(2)
    print("eating break fast")


def drink():
    time.sleep(2)
    print(f"Drinking coffee")


def study():
    time.sleep(2)
    print("Studying my homework")


# eatBreakFast()
# drink("Coffee")
# study()

thread1 = threading.Thread(target=eatBreakFast)
thread2 = threading.Thread(target=drink)
thread3 = threading.Thread(target=study)

thread1.start()
thread2.start()
thread3.start()

# thread synchronization : when a calling thread wait for a child thread to finish instruction execution and move on to the next instructions
thread1.join()
thread2.join()
thread3.join()

# Main thread is the in charge of all the threads
# returns the no. of currently running threads
print(threading.active_count())

# returns the list of all the threads
print(threading.enumerate())

# returns the no. of seconds taken by the main thread to finish the instruction execution inside the main thread
print(time.perf_counter())
