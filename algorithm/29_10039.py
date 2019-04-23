import sys
score = []
for i in range(5):
    num = int(sys.stdin.readline().rstrip())
    if num < 40:
        num = 40
    score.append(num)

print(int(sum(score)/len(score)))
