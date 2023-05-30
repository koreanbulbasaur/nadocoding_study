def profile(name, age, main_lang):
    print(f"이름 : {name}\t나이: {age}\t주 사용 언어: {main_lang}")


profile("현용범", 33, "파이썬")
profile("이현", 63, "자바")


def profile_1(name, age=17, main_lang="c++"):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")


profile_1("미누")
profile_1("윤가현")
