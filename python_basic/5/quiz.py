from random import *
ID = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
      15, 16, 17, 18, 19, 20]

shuffle(ID)

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {ID[0]}")
print(f"커피 당첨자 : {ID[1:4]}")
print("-- 축하합니다 --")
