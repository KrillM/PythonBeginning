# w -> 쓰기
#score_file = open("score.txt","w",encoding="utf-8")
#print("Math: 80", file=score_file)
#print("English: 85", file=score_file)

# a -> 이어쓰기
# score_file = open("score.txt","a",encoding="utf-8")
# score_file.write("Science: 85")
# score_file.write("\nProgramming: 90")
# score_file.close()

#  r -> 읽기
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# 한 줄씩 출력
# score_file = open("score.txt", "r", encoding="utf-8")
# for i in range(1, 5):
#     print(score_file.readline(), end="") # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
#
# while True:
#     line = score_file.readline()
#     if not line: break
#     print(line)
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()