class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, action):
        Animal.__init__(self, name)
        self.action = action

    def run(self):
        print("{0} is {1}". format(self.name, self.action))


class Poodle(Dog):
    def __init__(self, name, action):
        Dog.__init__(self, name, action)

    def run(self, color):
        print("{0} is {1}". format(self.name, color))

poodle = Dog("Poodle", "Run")
poodle.run()

mont = Poodle("Mont", "Run")
mont.run("Brown")

class Cat(Animal):
    def __init__(self, name, action):
        pass

coco = Cat("Coco", "Run")
