
import sys
n = int(sys.stdin.readline())
value = []
for i in range(n):
    value.append(int(sys.stdin.readline()))
value.sort(reverse = True)
weight = []

while value:
    a = len(value) * value.pop()
    weight.append(a)

print(max(weight))
