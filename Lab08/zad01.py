from multiprocessing import *
from time import sleep


def task():
    sleep(1)
if __name__ == '__main__':
    proces =  Process(target=task)
    print(proces.exitcode)
    print(proces.name)
    print(proces.daemon)
    print(proces.pid)
    proces.start()
    print(proces.exitcode)
    print(proces.pid)
    print(proces.is_alive())
    proces.join()
    print(proces.exitcode)
