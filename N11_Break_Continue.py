absent = [2,5]

for c in range(1,11):
    if c in absent:
        continue
    print(c)

idx = 10
while idx > 0:
    if idx == 5:
        break
    print(idx)
    idx-=1