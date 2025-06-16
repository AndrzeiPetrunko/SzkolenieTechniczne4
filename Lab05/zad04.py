def decorator_metody(func):
    def metoda(self):
        func(self)
        print("cos")
    return metoda

class Klasa:
    @decorator_metody
    def elo(self):
        print("cześć")
k1 = Klasa()
k1.elo()
