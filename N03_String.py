# 1. 문자열

sentence = 'I am a boy.'
sentence2 = "Python is easy."

sentence3 = """I am a boy.
Python is easy.
"""

print(sentence3)

# 2. 슬라이싱
idNumber = "061125-3456789"
print(idNumber[7]) # Gender
print(idNumber[0:2]) # Birth Year
print(idNumber[:2]) # Birth Year
print(idNumber[-7:]) # Birth Year

# 3. 문자열 처리 함수
# lower, upper, isupper, islower, len, replace, find, index, count
python = "Python is Amazing."
index = python.index("n")
print(index)

# 4. 문자열 포멧
print("I am a %d years old" % 20)
print("I am a {} years old" .format(20))

print("I like %s" % "Python")
print("I got %c" % 'A')

print("My favorite menus: %s, %s" % ("Hamburger", "Ramen"))
print("My favorite menus: {}, {}" .format("Hamburger", "Ramen"))
print("My favorite menus: {1}, {0}" .format("Hamburger", "Ramen"))

print("I am {age} years old and I am {club}" .format(age = 20, club = "Gooner"))



