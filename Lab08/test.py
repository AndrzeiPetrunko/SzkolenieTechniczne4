import multiprocessing
# from time import sleep
# from random import random
# from multiprocessing import Process
# from multiprocessing import RLock
#
# # reporting function
# def report(lock, identifier):
#     with lock:
#         print(f'>process {identifier} done')
#
#
#
# def task(lock, identifier, value):
#     # acquire the lock
#     with lock:
#         print(f'>process {identifier} sleeping for {value}')
#         sleep(value)
#         # report
#         report(lock, identifier)
#
#
# if __name__ == '__main__':
#     # create a shared reentrant lock
#     lock = RLock()
#     # create processes
#     processes = [Process(target=task, args=(lock, i, random())) for i in
#                  range(10)]
#     # start child processes
#     for process in processes:
#         process.start()
#     # wait for child processes to finish
#     for process in processes:
#         process.join()

from multiprocessing import Process

def funkcja(i):
    print("Proces", i)
if __name__ == '__main__':
    for i in range(5):
        p = Process(target=funkcja, args=(i,))
        p.start()


