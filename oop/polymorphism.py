class Dog:
    def sound(self):
        print("Generic sound")


class Labrador(Dog):
    def sound(self):
        print("Labrador sound")


class Golden(Dog):
    pass


max = Labrador()
tom = Golden()

max.sound()
tom.sound()
