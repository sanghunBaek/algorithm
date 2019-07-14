# 파이썬 반복문에서는 return 을 쓸 수 없다고함
import sys
num = int(sys.stdin.readline().rstrip())
total = num

def checkgnum(a):
    count = 0
    result = []
    for i in range(len(a)):
        if a[i] not in result:
            result.append(a[i])
        else:
            if a[i] == a[i - 1]:
                continue
            else:
                count = -1
                break
    return count


for i in range(num):
    cvalue = sys.stdin.readline().rstrip()
    total = total + checkgnum(cvalue)


print(total)
