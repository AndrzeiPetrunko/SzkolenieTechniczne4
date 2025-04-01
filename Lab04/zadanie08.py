class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Niewolnik:
    def __init__(self, aaa):
        self.aaa =aaa

class MetaDodajNiewolnika(type):
    def __new__(cls, name, bases, class_dict):
        if Osoba in bases:
            bases = bases + (Niewolnik,)
            print(bases)
        return super(MetaDodajNiewolnika, cls).__new__(cls, name, bases, class_dict)

class Pracownik(Osoba, metaclass=MetaDodajNiewolnika):
    def __init__(self, imie, nazwisko, stanowisko):
        super().__init__(imie, nazwisko,aaa)
        self.stanowisko = stanowisko

pracownik = Pracownik("Jan", "Kowalski", "Inżynier",222)

print(pracownik.__class__.__bases__, pracownik.__dict__, Pracownik.__dict__)
print(pracownik.aaa)