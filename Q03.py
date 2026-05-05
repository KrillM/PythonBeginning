address = "https://naver.com"
index = address.index("/")
index = address.index("/", index + 1)

address = address.replace(address[:index + 1], "")

index = address.index(".")
address = address.replace(address[index:], "")

num = len(address)
eCount = address.count("e")

pw = address[:3] + str(num) + str(eCount) + "!"
print(pw)