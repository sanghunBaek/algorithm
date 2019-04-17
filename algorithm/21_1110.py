# 배열 = 할때 온전하게 값만 가는게 아니라 위치가 가는거라서?
# =을 함부러 주면 안된다 그래서 copy를 써주는거
# from copy import copy 해주고 a = copy(b) 이렇게
import sys
from copy import copy

num = sys.stdin.readline().rstrip()
value = []
count = 0
chvalue = [0, 0]
if len(num) == 1:
    value.append(0)
    value.append(int(num))
else:
    value.append(int(num[0]))
    value.append(int(num[1]))

origin = copy(value)

while 1:
    chvalue[0] = value[1]
    chvalue[1] = (value[1] + value[0]) % 10
    count = count + 1
    if (origin[0] == chvalue[0]) and (origin[1] == chvalue[1]):
        break
    value = copy(chvalue)
    chvalue  = [0, 0]


print(count)

