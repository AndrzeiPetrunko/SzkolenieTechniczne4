from zadanie03 import Meta
class A(metaclass=Meta):
    pass
class B(metaclass=Meta):
    pass

print(A.attr, B.attr)