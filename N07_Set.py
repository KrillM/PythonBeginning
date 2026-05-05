# 중복을 허용하지 않고 순서가 없다.
set = {1,2,3,3,3,4,5}
print(set)

fe = {"yena", "jisu", "asahi"}
be = {"krille", "eden", "yena"}

# 교집합
print(fe & be) # and는 안 된다.
print(fe.intersection(be))

# 합집합
print(fe | be) # or도 안 된다.
print(fe.union(be))

# 차집합
print(fe - be)
print(fe.difference(be))

be.add("sooah")
print(be)

be.remove("eden")
print(be)