def add_info_method(cls):
    def info(self):
        print("Składniki klasy:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")
    cls.info = info
    return cls

@add_info_method
class Klasa:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

# Tworzymy obiekt
k1 = Klasa("1", "2", 3)

# Wywołujemy metodę info
k1.info()
