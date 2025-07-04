class Cos:
    attr = 1000
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


Klasa = type('Klasa', (Cos,), {'attr': 100})
y = Klasa()
print(y.__class__.__bases__)

class Tam:
    pass

def f(obj):
    return obj.age
def nnw(cls):
    x = object.__new__(cls)
    x.attr = 13
    x.age = 1
    x.f = f
    return x
Tam.__new__ = nnw

tam = Tam()
print(tam.attr)
print(tam.age)
print(tam.f)

class Meta(type):
    def __new__(cls, name, bases, dct):
        xx = super().__new__(cls, name, bases, dct)
        xx.attr = 100
        return xx