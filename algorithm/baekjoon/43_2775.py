from copy import copy
import sys

num = int(sys.stdin.readline().rstrip())
result = []
def makefloor(floor,ho):
    basefloor = [i for i in range(1, 15)]
    for i in range(floor):
        resultfloor = []
        for j in range(len(basefloor)):
            resultfloor.append(sum(basefloor[:j + 1]))
        basefloor = copy(resultfloor)
    return basefloor[ho-1]


for i in range(num):
    floor = int(sys.stdin.readline().rstrip())
    ho = int(sys.stdin.readline().rstrip())
    result.append(makefloor(floor,ho))

for i in range(len(result)):
    print(result[i])


