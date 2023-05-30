# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

meat = {"소고기", "돼지고기", "닭고기"}
favorite = set(["돼기고기", "오리고기"])

# 교집합
print(meat & favorite)
print(meat.intersection(favorite))

# 합집합
print(meat | favorite)
print(meat.union(favorite))
