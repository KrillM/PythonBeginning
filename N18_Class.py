class Unit:
    def __init__(self, name, hp, damage): # __init__ : 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} is generated".format(self.name))
        print("HP: {0}, Attack: {1}".format(self.hp, self.damage))

# Marine = Unit("Marine", 40, 5)
# Tank = Unit("Tank", 150, 35)

Wraith1 = Unit("Wraith", 80, 5)
print(Wraith1.name)
print(Wraith1.hp)

Wraith2 = Unit("Steel Wraith", 80, 5)
Wraith2.clocking = True

# 파이썬은 외부에서 맴버변수를 선언할 수 있다.
if Wraith2.clocking:
    print(Wraith2.name +" is clocked")