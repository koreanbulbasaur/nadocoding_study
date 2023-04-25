score_file = open(
    r'C:\Private_Projects\nadocoding\python_basic\8\score.txt', 'w', encoding="utf8")
print("나 졸았어", file=score_file)
print("코까지 골았어", file=score_file)
print("부끄럿!", file=score_file)

score_file.close()
