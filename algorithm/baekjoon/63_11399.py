# 시간이 달라지는이유
# 앞에서 많이 걸리는 사람있으면 뒤에사람들이 기다리는 시간 늘어남
# 즉 빨리하는사람이 앞이면 최소시간되는것

# 1. 최소순으로 돌림
# 2. 각각의 합
# 1까지합 2까지합 3까지합 이런식으로해서 총합을 구해야한다.


import sys

n = int(input())
value = list(map(int,sys.stdin.readline().split(" ")))
value.sort()
b = [0]*n
for i in range(n):
    b[i] = sum(value[0:i+1])
print(sum(b))