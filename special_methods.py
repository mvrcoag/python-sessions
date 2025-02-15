"""
class Figure:
    def __init__(self, color):
        self.color = color

class Square(Figure):
    def __init__(self, color):
        super(color) -- Executes Figure.__init__(color)

        Figure.__init__(color)
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.verbose = False

    # Str representation
    def __str__(self):
        return f"{self.name} {self.age}"

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"

    # Operator overloading
    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age

    def __truediv__(self, other):
        return self.age / other.age

    def __floordiv__(self, other):
        return self.age // other.age

    def __mod__(self, other):
        return self.age % other.age

    def __pow__(self, other):
        return self.age**other.age

    # Attribute access

    # Existing attributes
    def __getattribute__(self, attr_name):
        if super().__getattribute__("verbose") == True:
            print(f"Accessing to {attr_name}")

        return super().__getattribute__(attr_name)

    # Non-existing attributes
    def __getattr__(self, attr_name):
        if attr_name == "left_years":
            return 100 - self.age

        return super().__getattr__(attr_name)

    def __delattr__(self, attr_name):
        raise AttributeError("can not delete attributes: " + attr_name)

    def switch_verbose(self):
        self.verbose = False if self.verbose == True else True


john = Person("John Doe", 20)

print(john.left_years)

del john.age

print(john.name)
