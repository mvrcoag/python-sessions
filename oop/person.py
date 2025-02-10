class Person:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill
        self.friends = []

    def greet(self, name):
        return f"Hello {name}"

    def add_friend(self, person):
        self.friends.append(person)

    def format_friend_names(self):
        if len(self.friends) == 0:
            return "You don't have friends!"

        names = []

        for i in range(len(self.friends)):
            names.append(self.friends[i].name)

        return ", ".join(names)


marco = Person("Marco", 21, lambda: print("Code"))
pedro = Person("Pedro", 40, lambda: print("Swim"))
juan = Person("Juan", 40, lambda x: print(f"Play {x}"))

marco.add_friend(pedro)
marco.add_friend(juan)

marco.skill()
pedro.skill()
juan.skill("Tenis")
