class InputError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

try:
    x = int(input("첫번째 숫자"))
    y = int(input("두번째 숫자"))
    if x >= 10 or y >= 10:
        raise InputError("입력값: {0}, {1}".format(x, y))
    print(x+y)
except ValueError:
    print("잘못된 값 입력!")
except InputError as err:
    print("에러가 발생했습니다.")
    print(err)
finally:
    print("안뇽~~")