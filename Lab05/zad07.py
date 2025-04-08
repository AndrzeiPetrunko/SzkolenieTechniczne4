class CRUD:
    Object = None
    def __init__(self, num):
        self.num = num
    @staticmethod
    def create():
        return  "Created"
    @staticmethod
    def read():
        return "Read"
    @staticmethod
    def update():
        return "Updated"
    @staticmethod
    def delete():
        return "Deleted"
    @classmethod
    def setObject_value(cls, value):
        cls.Object = value
        print("Object is set,", cls.Object)
    @property
    def num_squared(self):
        return self.num ** 2


print(CRUD.create())
print(CRUD.read())
print(CRUD.update())
print(CRUD.delete())
CRUD.setObject_value("Hello")
C = CRUD(5)
print(C.num)
print(C.num_squared)
