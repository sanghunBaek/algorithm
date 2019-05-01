# 생각보다 쉬웠음 결국은 같은게 몇개 있느냐에 집중해서 문제를 풀었다

import sys
a = sys.stdin.readline().rstrip()

a = a.replace("9","6")
count = 0
doublelist = []

for i in set(a):
    if i != "6":
        doublelist.append(a.count(i))
    else:
        doublelist.append(a.count(i)//2 + a.count(i)%2)

value = max(doublelist)
print(value)