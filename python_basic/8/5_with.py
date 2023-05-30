with open(r"C:\Private_Projects\nadocoding\python_basic\8\study.txt",
          "w", encoding="utf8") as study_file:
    study_file.write("코를 골다니... 나가서 뒈지고 싶네...")

with open(r"C:\Private_Projects\nadocoding\python_basic\8\study.txt",
          "r", encoding="utf8") as read_file:
    print(read_file.read())
