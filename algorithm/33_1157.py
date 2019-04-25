# 증복을 제거하는 set 같은 집합은 순서가 없다. 그래도 for문으로 사용할 수 는 있다
import sys
a = sys.stdin.readline().rstrip().upper()
result = []
charlist = []

b = set(a)
for i in b:
    result.append(a.count(i))
    charlist.append(i)

maxnum = max(result)

if result.count(maxnum) != 1:
    print("?")
else:
    indexmax = result.index(maxnum)
    print(charlist[indexmax])





