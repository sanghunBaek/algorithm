# for문으로 print로 출력할때 한줄에 출력하기 위해서는 print문 뒤에 end = ' ' 써주면된다

import sys

info = sys.stdin.readline().rstrip().split(" ")
num = sys.stdin.readline().rstrip().split(" ")

info = list(map(int, info))
num = list(map(int, num))
result = []

for i in range(info[0]):
    if info[1] > num[i]:
        result.append(num[i])

for i in range(len(result)):
    print(result[i],end = ' ')