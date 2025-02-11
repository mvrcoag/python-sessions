from abc import ABC, abstractmethod


class Dog(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Labrador(Dog):
    def sound(self):
        print("Labrador sound")


class Beagle(Dog):
    def sound(self):
        print("Beagle sound")


max = Beagle("Max")
max.sound()

tom = Labrador("Tom")
tom.sound()
