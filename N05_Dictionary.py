# dictionary -> key : value, 중복 불가

cabinet = {3: "krille", 10: "eden", 45: "jisu"}
print(cabinet[10])
print(cabinet.get(3))

#print(cabinet[18]) # Error
print(cabinet.get(18)) # None 출력
print(cabinet.get(18, "Guest")) # Guest 출력
print("hi")

print(3 in cabinet)
print(18 in cabinet)
print(20 in cabinet)

# 추가
cabinet[47] = "donald"
print(cabinet)
print(cabinet[47])

# update
cabinet[10] = "hazard"
print(cabinet)
print(cabinet[10])

# remove
del cabinet[10]
print(cabinet)

# key만 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)