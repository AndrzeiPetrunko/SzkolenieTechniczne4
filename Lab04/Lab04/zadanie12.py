
class Nazewnik(type):
    def __new__(cls, name, bases, class_dict):
        # Sprawdzanie nazwy klasy
        if not name[0].isupper():
            name = name[0].upper() + name[1:]
            print(f"Poprawiono nazwę klasy na: {name}")

        for attr in list(class_dict.keys()):
            if not attr[0].islower():
                new_attr = attr[0].lower() + attr[1:]
                class_dict[new_attr] = class_dict.pop(attr)
                print(f"Poprawiono nazwę zmiennej: {attr} na {new_attr}")

        for attr in list(class_dict.keys()):
            if callable(class_dict[attr]) and not attr[0].isupper():
                new_attr = attr[0].upper() + attr[1:]
                class_dict[new_attr] = class_dict.pop(attr)
                print(f"Poprawiono nazwę metody: {attr} na {new_attr}")

        return super().__new__(cls, name, bases, class_dict)


class Osoba(metaclass=Nazewnik):
    imie = "Jan"
    nazwisko = "Kowalski"

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}")


class Pojazd(metaclass=Nazewnik):
    marka = "Toyota"
    model = "Corolla"

    def wyswietl_info(self):
        print(f"Marka: {self.marka}, Model: {self.model}")


osoba = Osoba()
pojazd = Pojazd()

osoba.przedstaw_sie()
pojazd.wyswietl_info()
