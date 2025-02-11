class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's name: {self.name}")


class Labrador(Dog):
    def sound(self):
        print("Labrador sound")


# Single
# Multilevel
# Multiple

tom = Labrador("Tom")
tom.display_name()

# Multilevel


class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} Guide the way")


max = GuideDog("Max")

max.display_name()

# Multiple


class Friendly:
    def greet(self):
        print("Friendly God")


class GoldenRetriever(Dog, Friendly):
    def sound(self):
        print(f"Golden sound")


ray = GoldenRetriever("Ray")

ray.greet()  # Comes from friendly
ray.display_name()  # Comes from Dog
