# input은 항상 문자열을 받으므로 정수나 실수를 받을 때 int, double로 감싸준다.
score = int(input("Enter score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")