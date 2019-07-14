# reverse 는 알아서 역순으로 만들어 저장까지 해버림 이거 자체는 none으로 리턴
# join 을 통해서 리스트 합칠 수 있음 "".join(b) 이런식으로
import sys
a = sys.stdin.readline().rstrip()
result = []
a = a.split(" ")

for i in range(2):
    b = [j for j in a[i]]
    b.reverse()
    result.append(int("".join(b)))

print(max(result))
