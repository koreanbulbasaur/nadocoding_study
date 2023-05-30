import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"코딩": 100, "영어": 20, "수학": 80}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = 10
print(type(answer))
print("입력하신 값은", answer, "입니다")
