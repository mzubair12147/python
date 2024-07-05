"""
daemon thread : a thread that runs in the background and is not important for program execution
your program will not wait for daemon threads to complete before existing
non-daemon cannot normally be killed , stay alive until task is completed
"""

import threading
import time


def timer():
    count = 0
    while True:
        time.sleep(1)
        print(f"logged in for {count} seconds")
        count += 1


# The daemon thread will continue running until there are non daemon threads running in the program
# when there are no non-daemon threads running in the background. the running daemon threads will automatically be killed
# login_Time = threading.Thread(target=timer, daemon=True)
login_Time = threading.Thread(target=timer)

# you cannot change the demon property during thread execution. so you have to change it before starting the thread.
# btw! this method id deprecated
login_Time.setDaemon(True)
login_Time.start()
print("login_time thread is daemon: {}".format(login_Time.isDaemon()))
ask = input("Do you want to exit?: ")
