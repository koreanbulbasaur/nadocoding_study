def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("미누", 25, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("현용범", 33, "kotlin", "Swift")
