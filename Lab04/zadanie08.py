class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Niewolnik:
    def __init__(self):
        pass

class MetaDodajNiewolnika(type):
    def __new__(cls, name, bases, class_dict):
        if Osoba in bases:
            bases = bases + (Niewolnik,)
        return super().__new__(cls, name, bases, class_dict)

class Pracownik(Osoba, metaclass=MetaDodajNiewolnika):
    def __init__(self, imie, nazwisko, stanowisko):
        super().__init__(imie, nazwisko)
        self.stanowisko = stanowisko

pracownik = Pracownik("Jan", "Kowalski", "Inżynier")

print(pracownik.__class__.__bases__)