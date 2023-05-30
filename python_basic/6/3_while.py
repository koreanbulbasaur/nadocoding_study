"""
customer = "미누"
index = 5
while index >= 1:
    print(f"{customer}님, 커피가 준비 되었습니다. {index}")
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")
"""

customer = "현용범"
person = "Unknown"

while person != customer:
    print(f"{customer}, 커피가 준비되었습니다.")
    person = input("이름이 어떻게 되세요?> ")
