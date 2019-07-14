import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
valueLS = []
def isItSosu(num):
    count = 0
    if num == 1:
        return False

    for i in range(1,num):
        if num % i == 0:
            count += 1
    if count == 1 :
        return True

for i in range(m,n+1):
    if isItSosu(i):
        valueLS.append(i)
if len(valueLS) == 0:
    print(-1)
else:
    print(sum(valueLS))
    print(valueLS[0])