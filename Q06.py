def std_weight(gender, height):
    standard_weight = 0
    heightH = height/100

    if gender == "남자":
        standard_weight = heightH * heightH * 22
    else :
        standard_weight = heightH * heightH * 21

    standard_weight = round(standard_weight, 2)
    print("키 " + str(height)+" " + gender +"의 표준 체중은 "+str(standard_weight)+"kg 입니다")


std_weight("남자", 175)
std_weight("여자", 165)
