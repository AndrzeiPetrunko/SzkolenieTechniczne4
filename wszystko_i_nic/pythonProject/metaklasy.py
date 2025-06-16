class Metakalsa(type):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        def metoda(self):
            print("metodad działa")
        obj.metoda = metoda
        obj.atrybut = 100
        return obj


    #створення метакласи без ніхуя
class A(metaclass=Metakalsa):
    pass
a = A()
a.metoda()
print(a.atrybut)