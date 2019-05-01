# 그냥 쭉 카운팅하는게 어떨까? 규칙을 찾으려고 했는데 규칙은 정말 안나옴
# 하나씩 올리고 그때 비교하고 그러면서 카운팅하는식으로?
# 리미트 두고

# 음 일단 답은 나오는데 시간초과임 .. 어떻게 해야하지
# 일단 예상가는 원인은 값이 아닌거를 너무 늦게 찾아내서? 일단 지금은 일일이 확인하는 식이니까
# 다른 규칙이 있나 내가 모르는?

import sys

loopnum = int(sys.stdin.readline().rstrip())
result = []

def checkit(m,n,k,z):
    x = 1
    y = 1
    count = 1

    # check = abs(k-z)%(m-n)

    while 1:
        if x == m and y == n:
        # if check != 0:
            return -1
        if k == x and z == y:
            return count

        if x + 1 > m:
            x = 1
        else:
            x = x + 1

        if y + 1 > n:
            y = 1
        else:
            y = y + 1

        count = count + 1

for i in range(loopnum):
    num = sys.stdin.readline().rstrip().split(" ")
    num = list(map(int, num))
    result.append(checkit(num[0],num[1],num[2],num[3]))

for i in range(len(result)):
    print(result[i])


