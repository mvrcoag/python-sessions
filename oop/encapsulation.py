# Encapsulation
# Public
# Protected
# Private


class Dog:
    def __init__(self, name, age, color):
        if not self.__is_valid_color(color):
            return

        self.name = name
        self._age = age
        self.__color = color

    def get_info(self):
        return f"{self.name}: {self._age} years, color {self.__color}"

    # Getter
    def get_color(self):
        return self.__color

    # Setter
    def set_color(self, color):
        if not self.__is_valid_color(color):
            return

        self.__color = color

    def __is_valid_color(self, color):
        colors = ["white", "black", "brown"]
        if color not in colors:
            print("Invalid color")
            return False


max = Dog("Max", 5, "black")
max.__is_valid_color("red")
