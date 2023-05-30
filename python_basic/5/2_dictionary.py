cabinet = {1: "미누", 33: "현용범"}
print(cabinet[1])
print(cabinet[33])

print(cabinet.get(1))
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(1 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"M-1": "Minu", "H-33": "현용범"}
print(cabinet["M-1"])
print(cabinet["H-33"])

print(cabinet)
cabinet["M-3"] = "이현"
cabinet["B-25"] = "바다거"
print(cabinet)

del cabinet["M-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items)

cabinet.clear()
print(cabinet)
