class Roślina(type):
    def __new__(cls, name, bases, class_dict):
        allowed_attributes = ['energetyczna', 'pastewna', 'rekultywacyjna', 'ozdobna']
        attributes = [attr for attr in allowed_attributes if attr in class_dict]

        if len(attributes) > 1:
            raise ValueError(
                "Nowa roślina może mieć tylko jeden z atrybutów: 'energetyczna', 'pastewna', 'rekultywacyjna', 'ozdobna'.")

        return super().__new__(cls, name, bases, class_dict)


class RoślinaBazowa(metaclass=Roślina):
    pass


class Kwiat(RoślinaBazowa):
    energetyczna = True
    pastewna = True  


class Drzewo(RoślinaBazowa):
    rekultywacyjna = True


try:
    kwiat = Kwiat()
except ValueError as e:
    print(e)

drzewo = Drzewo()
print("Drzewo zostało utworzone pomyślnie.")
