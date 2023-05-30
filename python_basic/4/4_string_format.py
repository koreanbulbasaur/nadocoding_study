print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "감자튀김")
print("Apple 은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("빨간", "검정"))

print("나는 {}살입니다.".format(33))
print("나는 {}색과 {}색을 좋아해요.".format("초록", "검정"))
print("나는 {0}색과 {1}색을 좋아해요.".format("초록", "검정"))
print("나는 {1}색과 {0}색을 좋아해요.".format("초록", "검정"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=33, color="검정"))

age = '성우'
name = '이현'
print(f"나는 {age}살이며, 이름은 {name}이야.")
