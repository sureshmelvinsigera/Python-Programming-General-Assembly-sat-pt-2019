class Animal:
    def __int__(self):
        print("Animal is created")

    def who(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self, name):
        super().__int__()
        self.name = name
        print("creating a dog name ", self.name)


sophie = Dog("sophie")
