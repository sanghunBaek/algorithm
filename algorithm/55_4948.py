import sys

value = 1
totalResult = []

num = [x for x in range(1, 2 *123456 + 1)]
num.insert(0, 1)
for i in range(2, 2 *123456 + 1):
    j = 2
    while 2 * 123456 >= i * j:
        num[i * j] = 1
        j += 1

def checkCS(n):
    count = 0
    for l in num:
        if l > 2*n:
            return count

        if l!=1 and n<l:
            count += 1
    return count

while value != 0:
    value = int(sys.stdin.readline())
    totalResult.append(checkCS(value))

totalResult.pop()
for i in range(len(totalResult)):
    print(totalResult[i])

