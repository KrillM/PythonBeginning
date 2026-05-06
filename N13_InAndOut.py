print("Python", "Java", sep=", ", end=".")
print("hello")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 에러

# 딕셔러니에서만 가능한 for 문
scores = {"Math": 80, "English": 70, "Programming": 95}
for subject, score in scores.items():
    print(subject.ljust(12), str(score).rjust(2), sep=": ")

# 자리 맞추기
for number in range(1, 21):
    print("대기번호 : "+ str(number).zfill(3))

answer = input("단어를 입력하세요 : ")
print(answer)