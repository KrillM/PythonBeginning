# 일반
try:
    x = int(input("첫번째 숫자"))
    y = int(input("두번째 숫자"))
    print(x+y)
except ValueError:
    print("입력값 에러!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

# 의도된 에러
try:
    x = int(input("첫번째 숫자"))
    y = int(input("두번째 숫자"))
    if x >= 10 or y >= 10:
        raise ValueError
    print(x+y)
except ValueError:
    print("잘못된 값 입력!")