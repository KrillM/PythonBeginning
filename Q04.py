from random import *

classRoom = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
chicken = randint(1,len(classRoom))
#print(chicken)

classRoom.remove(chicken)
#print(classRoom)

coffee_list = []

coffee1 = randrange(1,len(classRoom))
#print(coffee1)
c1 = classRoom[coffee1]
#print(c1)
coffee_list.append(c1)
classRoom.remove(c1)

coffee2 = randrange(1,len(classRoom))
#print(coffee2)
c2 = classRoom[coffee2]
#print(c2)
coffee_list.append(c2)
classRoom.remove(c2)

coffee3 = randrange(1,len(classRoom))
#print(coffee3)
c3 = classRoom[coffee3]
#print(c3)
coffee_list.append(c3)
classRoom.remove(c3)

#print(coffee_list)
coffee_list.sort()
#print(coffee_list)


print("치킨 당첨자 : " + str(chicken))
print("커피 당첨자 : " + str(coffee_list))