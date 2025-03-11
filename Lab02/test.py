class Cos:
    pass
obj = Cos()
obj.__class__
type(obj)
print(obj.__class__ is type(obj))

n = 5
d = {'x' : 1, 'y' : 2}
x = Cos()
for obj in (n, d, x):
    print(obj.__class__ is type(obj))

def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x

Cos.__new__ = new
f = Cos()
print(f.attr)
g = Cos()
print(g.attr)