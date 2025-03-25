class Roślina(type):
    def __new__(cls, name, bases, class_dict):
        attributes_to_remove = ['mięśnie', 'nerwy', 'oczy', 'skóra']

        for attr in attributes_to_remove:
            if attr in class_dict:
                del class_dict[attr]

        return super().__new__(cls, name, bases, class_dict)


class RoślinaBazowa(metaclass=Roślina):
    pass


class Kwiat(RoślinaBazowa):
    mięśnie = True
    nerwy = True
    kolor = "czerwony"


class Drzewo(RoślinaBazowa):
    skóra = True
    wysokość = 5


kwiat = Kwiat()
drzewo = Drzewo()

print(f"Kwiat posiada atrybuty: {dir(kwiat)}")
print(f"Drzewo posiada atrybuty: {dir(drzewo)}")
