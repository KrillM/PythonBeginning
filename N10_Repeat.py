# for
for i in range(1,11):
    print(i)

for i in ["Krille", "Yena", "Jisu", "Eden", "Asahi"]:
    print(i)

feTeam = ["Yena", "Jisu", "Asahi"]

for i in feTeam:
    print(i)

beTeam = ["Krille", "Yena", "Eden"]
beTeam = [len(i) for i in beTeam]
print(beTeam)

# while
index = 5

while index >= 0:
    print(index)
    index -= 1
    if index == 0:
        print("Finish")
        break