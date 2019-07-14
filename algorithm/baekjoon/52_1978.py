import sys
num = int(sys.stdin.readline())
a = sys.stdin.readline().rstrip()
a = a.split(" ")
count = 0
a = list(map(int,a))

def isItSosu(num):
    count = 0
    if num == 1:
        return False

    for i in range(1,num):
        if num % i == 0:
            count += 1
    if count == 1 :
        return True

for i in a:
    if isItSosu(i):
        count += 1

print(count)




