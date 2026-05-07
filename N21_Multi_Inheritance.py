class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} attacks to {1}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : damaged {1}".format(self.name, damage))
        self.hp -= damage
        print("HP: {0}".format(self.hp))

        if self.hp <= 0 :
            print("{0} wasted".format(self.name))

class Flyable:
    def __init__(self, speed):
        self.speed = speed

    def fly(self, name, location):
        print("{0} fly to {1} [{2} km/h]".format(name, location, self.speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)


Valkyrie = FlyableAttackUnit("Valkyrie", 200,6,5)
Valkyrie.fly(Valkyrie.name, "west")