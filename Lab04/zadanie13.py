import os
import time
import threading


class Plikownik(type):
    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        obj.filename = f"{obj.__class__.__name__}_{id(obj)}.txt"
        with open(obj.filename, "w") as f:
            for attr, value in obj.__dict__.items():
                f.write(f"{attr}: {value}\n")

        # Uruchamiamy wątek do automatycznego usunięcia obiektu po 10 sekundach
        threading.Thread(target=obj.auto_delete, daemon=True).start()
        return obj


class AutoDeleteMixin:
    def auto_delete(self):
        for i in range(10, 0, -1):  # Odliczanie czasu do usunięcia
            if not os.path.exists(self.filename):
                return
            print(f"Plik {self.filename} zostanie usunięty za {i} sekund...")
            time.sleep(1)
        self.__del__()

    def __del__(self):
        if hasattr(self, "filename") and os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"Plik {self.filename} został usunięty.")


class Osoba(AutoDeleteMixin, metaclass=Plikownik):
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Pojazd(AutoDeleteMixin, metaclass=Plikownik):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model


# Przykładowe użycie
osoba = Osoba("Jan", "Kowalski")
pojazd = Pojazd("Toyota", "Corolla")

print(f"Plik utworzony: {osoba.filename}")
print(f"Plik utworzony: {pojazd.filename}")
