###

def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper


@simple_decorator
def say_hello():
    print("Hello!")


say_hello()


###

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"


print(greet("Karishma"))


###

# *args example
def fun(*args):
    return sum(args)


print(fun(1, 2, 3, 4))
print(fun(5, 10, 15))


# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)


fun(a=1, b=2, c=3)

###

def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper

@decorator_one
@decorator_two
def say_goodbye():
    print("Goodbye!")
say_goodbye()

###

def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper
class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj = MyClass()
obj.say_hello()

###

def fun(cls):
    cls.class_name = cls.__name__
    return cls
@fun
class Person:
    pass
print(Person.class_name)

###

class Employee:
    raise_amount = 1.05
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
 # Using the class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)