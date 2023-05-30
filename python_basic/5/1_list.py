subway = [10, 20, 30]
print(subway)

subway = ["망고스틴", "애플망고", "딸기"]
print(subway)

print(subway.index("딸기"))

subway.append("골드키위")
print(subway)

subway.insert(1, "수박")
print(subway)

print(subway.pop())
print(subway)

subway.append("애플망고")
print(subway)
print(subway.count("애플망고"))

# ----------num_list----------
print("-"*10 + "num_list" + "-"*10)

num_list = [5, 2, 3, 1, 4]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [4, 2, 1, 5, 7]
mix_list = ["현용법", 33, True]

num_list.extend(mix_list)
print(num_list)
