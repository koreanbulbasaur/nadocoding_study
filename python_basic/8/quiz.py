for i in range(1, 51):
    report_file = open('C:/Private_Projects/nadocoding/python_basic/8/report/{}주차.txt'.format(i),
                       'w', encoding='utf8')
    print("- {} 주차 주간보고 -".format(i), file=report_file)
    print("부서 :", file=report_file)
    print("이름 :", file=report_file)
    print("업무 요약 :", file=report_file)

    report_file.close()
