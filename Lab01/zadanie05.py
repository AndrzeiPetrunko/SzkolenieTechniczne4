class Pojazd:
    def __init__(self, predkosc):
        self.predkosc = predkosc
    def give_info(self):
        print(f"Prędkość pojazdu wynosi {self.predkosc}")

class Samochod(Pojazd):
    def __init__(self, predkosc, pojemnosc):
        super().__init__(predkosc)
        self.pojemnosc = pojemnosc
    def give_info(self):
        print(f"Pojemność samochodu wynosi {self.pojemnosc}, prędkoćś: {self.predkosc}")
p1 = Pojazd(20)
s1 = Samochod(20, 20)
p1.give_info()
s1.give_info()