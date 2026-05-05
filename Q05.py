from random import *

# N09 ~ 11 : Condition, Repeat, Break, Continue

totalCustomer = 0

for i in range(1, 51):
    time_Custmomer = randint(5, 50)
    if(time_Custmomer >= 5 and time_Custmomer <= 15):
        print("[O] " + str(i)+"번째 손님 (소요시간 : "+str(time_Custmomer)+"분)")
        totalCustomer += 1
    else:
        print("[ ] " + str(i) + "번째 손님 (소요시간 : " + str(time_Custmomer) + "분)")

print("총 탑승 승객: "+str(totalCustomer))