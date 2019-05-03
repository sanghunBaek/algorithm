# 삽입 거품정렬 머시기라는데 파이썬은 sort로 끝

import sys
num = int(sys.stdin.readline().rstrip())
result = []
for i in range(num):
    value = int(sys.stdin.readline().rstrip())
    result.append(value)

result.sort()
for i in range(len(result)):
    print(result[i])
