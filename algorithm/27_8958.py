import sys

num = int(sys.stdin.readline().rstrip())
result = []

for i in range(num):
    result.append(sys.stdin.readline().rstrip())

def makesum(result):
    score = []
    for i in range(len(result)):
        if result[i] == "O":
            if result[i - 1] == "O" and i != 0:
                score.append(score[i - 1] + 1)
            else:
                score.append(1)
        else:
            score.append(0)
    return sum(score)


for i in range(len(result)):
    print(makesum(result[i]))