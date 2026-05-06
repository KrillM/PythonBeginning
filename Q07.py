# N13 ~ 17

for i in range(1, 11):
    report_file = open(str(i) + "주차.txt", "w", encoding="utf-8")
    report_file.write("- "+ str(i) +"주차 주간 보고 -")
    report_file.write("\n부서 : ")
    report_file.write("\n이름 : ")
    report_file.write("\n업무요약 : ")