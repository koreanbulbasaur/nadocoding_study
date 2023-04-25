def std_weight(gender, height):
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21


gender = "남자"
height = 192
weight = round(std_weight(gender, height / 100), 2)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")
