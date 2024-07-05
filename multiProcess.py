"""
multiprocessing : running tasks in parallel on different cpu cores, bypassing. bypassing gli used for multithreading. 
                multiprocessing : better for cpu bound tasks (heavy cpu usage)
                multithreading : better for io bound tasks (waiting around)
"""

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    # timestart = time.time()
    # a = Process(target=counter, args=(250000000,))
    # b = Process(target=counter, args=(250000000,))
    # a.start()
    # b.start()
    # a.join()
    # b.join()
    # timeend = time.time()
    # print(f"Finished in: {timeend - timestart} seconds")


if __name__ == "__main__":
    main()
