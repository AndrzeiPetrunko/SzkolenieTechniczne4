class Podatnik(type):
    def __new__(cls, name, bases, class_dict):
        class_dict['numer_nip'] = None
        return super().__new__(cls, name, bases, class_dict)

class Osoba(metaclass=Podatnik):
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Firma(metaclass=Podatnik):
    def __init__(self, nazwa):
        self.nazwa = nazwa


osoba = Osoba("Jan", "Kowalski")
firma = Firma("TechCorp")


osoba.numer_nip = "123-456-78-90"
firma.numer_nip = "987-654-32-10"

print(f"Osoba: {osoba.imie} {osoba.nazwisko}, NIP: {osoba.numer_nip}")
print(f"Firma: {firma.nazwa}, NIP: {firma.numer_nip}")
