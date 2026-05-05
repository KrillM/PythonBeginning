# List
train = [4, 10, 40]
print(train)
print(train.index(10))
print(train[2])

# append 맨 뒤
train.append(100)
print(train)

# insert (위치, 대상)
train.insert(2, 20)
print(train)

# 맨 뒤가 탈락
train.pop()
print(train)

train.append(10)
print(train.count(10))

# 정렬
num_list = [5,2,1,4,3]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

# 지우기
num_list.clear()
print(num_list)

# 확장
num_list = [5,2,1,4,3]
num_list.extend(train)
print(num_list)