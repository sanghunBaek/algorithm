import sys
number = []
result = 1

for i in range(3):
    number.append(int(sys.stdin.readline().rstrip()))
    result = result * number[i]

result = str(result)

for i in range(10):
    i = str(i)
    print(result.count(i))


