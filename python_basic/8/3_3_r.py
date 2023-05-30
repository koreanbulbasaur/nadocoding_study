"""
score_file = open(r"C:\Private_Projects\nadocoding\python_basic\8\score.txt", "r", encoding='utf8')
print(score_file.read())
score_file.close()
"""

score_file = open(
    r"C:\Private_Projects\nadocoding\python_basic\8\score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
