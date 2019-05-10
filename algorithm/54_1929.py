#에라토스테네스의 채 소수를 가장 빠르게 판별해내는 알고리즘이라고한다
#https://primes.utm.edu/glossary/page.php?sort=SieveOfEratosthenes

import sys
number = sys.stdin.readline().rstrip().split(" ")
number = list(map(int, number))

# m = 3
# n = 3

valueLS = []

def makeBesu(num,end):
    besuLS = []
    gop = 2
    a = num * gop
    while a <= end:
        besuLS.append(a)
        gop += 1
        a = num * gop
    return set(besuLS)

#흠 .. set은 순서가 없다는게 단점
# 차라리 for문 말고 while 써야할거 같은데 조건을 어떻게 줘야하지?
for i in range(number[0],number[1]+1):
    valueLS.append(i)

i = 0
while i < len(valueLS):
    num = valueLS[i]
    if num == 1:
        pass
        i += 1
    else:
        valueLS = set(valueLS)
        valueLS = valueLS - makeBesu(num,number[1])
        i += 1
        # print(valueLS)
        valueLS = list(valueLS)

valueLS.sort()
for i in range(len(valueLS)):
    print(valueLS[i])

# 아 ... 이게 1부터 시작하는게 아니면 이렇게 풀면 안되는구나