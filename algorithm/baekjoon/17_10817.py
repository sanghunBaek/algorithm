import sys

num = sys.stdin.readline().rstrip().split(" ")
num = list(map(int,num))

for i in range(len(num)-1):
    for j in range(1, len(num)):
        if num[i] < num[j]:
            a = num[i]
            num[i] = num[j]
            num[j] = a

print(num[1])



