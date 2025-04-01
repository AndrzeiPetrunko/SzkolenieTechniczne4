def dekorator_klasy(cls):
    cls.licznik_obiektow = 1
    print("zostal przypisany atrybut do klasy", cls.__name__)
    return cls
@dekorator_klasy
class Klasa:
    pass
k1 = Klasa()
print(k1.licznik_obiektow)