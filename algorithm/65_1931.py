n = int(input())
time = []
for i in range(n):
    x, y = map(int, input().split(" "))
    time.append((x,y))

cnt = 0
start_time = 0

time.sort(key = lambda time : time[0])
time.sort(key = lambda time : time[1])

for i,j in time:
    if i >= start_time:
        start_time = j
        cnt = cnt + 1

print(cnt)
