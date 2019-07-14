import sys
from collections import Counter

count = int(sys.stdin.readline())
a = []
for i in range(count):
    value = int(sys.stdin.readline())
    a.append(value)

#산술평균
print(round(sum(a)/len(a)))

#중앙값
a.sort()
mid = len(a)//2
print(a[mid])

# 라스트 최빈값
cnt = Counter(a)
b = cnt.most_common()
c = b[0][1]
d = []
for i,v in b:
    if v == c:
        d.append(i)
    else:
        break

d.sort()
if len(d) == 1:
    print(d[0])
else:
    print(d[1])

#범위
print(a[len(a)-1] - a[0])

