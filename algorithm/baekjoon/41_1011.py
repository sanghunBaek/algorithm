# 쉽게 생각했음 이게 결국은 그냥 개수를 구하는 거니까
# 그리고 최소거리니까 무조건 1씩 올라가는거임
# 마지막은 1이니까
# 결국 줄어들어서 1이 나와야함
# 그런걸 생각해주니까 다음과 같이 나왔음

import sys
num = int(sys.stdin.readline().rstrip())
valuelist = []

def findit(value):
    result = value[1] - value[0]
    inter = 1
    count = 0
    while result != 0:
        if result <= inter:
            count = count + 1
            return count
        else:
            if result >= 2 * inter:
                result = result - 2 * inter
                count = count + 2
                inter = inter + 1
            else:
                count = count + 2
                return count
    return count


for i in range(num):
    value = sys.stdin.readline().rstrip().split(" ")
    value = list(map(int,value))
    valuelist.append(findit(value))


for i in range(len(valuelist)):
    print(valuelist[i])






