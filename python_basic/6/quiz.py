from random import *
total_customor = []

for i in range(1, 51):
    minutes = randint(5, 51)
    if 5 <= minutes <= 15:
        print(f"[0] {i}번째 손님 (소요시간 :{minutes}분)")
        total_customor.append(i)
    else:
        print(f'[ ] {i}번째 손님 (소요시간 :{minutes}분)')

print(f'총 탑승 승객 : {len(total_customor)}')
