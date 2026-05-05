def open_account():
    print("New Account Printed")

open_account()

def calculator(x, y):
    return x + y

print(calculator(5, 6))

# 기본값
def classRoom(name, age = 15, subject = "C#"):
    print("{0} is {1} years old and study {2}".format(name, age, subject))

classRoom("krille")
classRoom("Yena")
classRoom("Eden")

# 가변인자
def classRoom2(name, *subject):
    print("{0} is 15 years old".format(name))
    for item in subject:
        print(item, end=" ")
    print()

classRoom2("krille", "English", "Physics", "Art")
classRoom2("Yena", "Math", "Algorithms", "Music")