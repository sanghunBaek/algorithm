# 흠 .. 이건일단 수학적 지식이 필요한 문제였음
# 각 자리 수의 합이 3의 배수가 된다는게 키포인트고
# 그냥 큰거순으로 하면 된다 .. ㅎ 그렇구나 난 엄청 어렵게 생각했는데
# 수학이 참 쉬운거구나


import sys
from collections import Counter

number = list(map(int,sys.stdin.readline().rstrip()))
# cnt = Counter(number)
# print(cnt)

def makeanw(number):
    if 0 in number:
        if sum(number)%3 == 0:
            number.sort(reverse = True)
            number = list(map(str,number))
            return "".join(number)
        else:
            return -1
    else:
        return -1

print(makeanw(number))




