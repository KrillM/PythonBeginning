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


fireBat1 = AttackUnit("FireBat", 50, 16)
fireBat1.attack("5'o Clock")
fireBat1.damaged(25)
fireBat1.damaged(25)