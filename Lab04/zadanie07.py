class OsobaMeta(type):
    def __new__(cls, name, bases, class_dict):
        if name in ["Student", "Wykladowca", "Dziecko"]:
            name = "Osoba"
        return super().__new__(cls, name, bases, class_dict)

class Student(metaclass=OsobaMeta):
    pass

class Wykladowca(metaclass=OsobaMeta):
    pass

class Dziecko(metaclass=OsobaMeta):
    pass

class Pojazd(metaclass=OsobaMeta):
    pass

print(Student.__name__)  # Osoba
print(Wykladowca.__name__)  # Osoba
print(Dziecko.__name__)  # Osoba
print(Pojazd.__name__)  # Pojazd