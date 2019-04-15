# sys.stdin.readline()가 input보다 빠르다고함 근데 이거하면 오른쪽 끝에 개행문까지 입력받아서 len으로 확인해보면 하나더 길어짐
# .rstrip()을통해서 오른쪽 공백을 지워줄 수 있다  sys.stdin.readline().rstrip()

import sys

t = int(sys.stdin.readline().rstrip())
a = []
for i in range(t):
    num = sys.stdin.readline().rstrip()
    num = num.split(" ")
    num = list(map(int, num))
    a.append(sum(num))

for i in range(len(a)):
    print(a[i])





