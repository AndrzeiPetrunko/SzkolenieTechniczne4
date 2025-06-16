def dedkorator_metody(metoda):
    def wrapper(*args):
        print("metoda zaczyna działanie")
        metoda(*args)
        print("metoda kończy działanie")
    return wrapper
@dedkorator_metody
def metoda(argument):
    print("Cos tam cos tam", argument)
metoda(8)


def dekorator_klasy(cls):
    cls.attr = 100
    def metoda_klasy(self, argument):
        print(argument * 12, "wynik mnożenia przez 12")
    cls.metoda_klasy = metoda_klasy
    return cls
@dekorator_klasy
class A:
    pass
a = A()
a.metoda_klasy(12)
print(a.attr)

