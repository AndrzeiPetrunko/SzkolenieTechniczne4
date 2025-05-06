# Zastosuj na swoich funkcjach dekoratory z pakietu HandyDecorators: trycatch, timer, sin
# gleton.
import time

import  decorators
from decorators import trycatch, timer


@trycatch
def division(a):
    print(a / 0)
#division(4)


@timer
def a():
    import time
    print('Hi')
    time.sleep(1)
a()