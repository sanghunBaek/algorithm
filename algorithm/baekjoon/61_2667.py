#https://itholic.github.io/kata-danji/
# 코드를 보면서 진짜 이렇게 할 수 도 있구나 라는걸 느꼈다 근데 사실 이게 DFS랑 먼상관인거지? 싶기는하다 그냥 재귀로 풀어서 그런가?
# 상관을 찾아보자면 BFS는 좀 넓게 주변부분들을 추가하고 계산하면서 가는 느낌이고
# DFS는 그냥 한개를 재귀로 깊게 판다는 느낌
# https://joosjuliet.github.io/2667/ 두가지 각각에 대한 코드
import sys

dx = [-1,1,0,0]
dy = [0,0,1,-1]
n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().rstrip()) for i in range(n)]

cnt = 0
apt = []

def dfs(x,y):
    global cnt
    matrix[x][y] = '0'
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny <0 or ny >= n:
            continue

        if matrix[nx][ny] == '1':
            dfs(nx,ny)


for i in range(n):
    for j in range(n):

        if matrix[i][j] == '1':
            cnt = 0
            dfs(i,j)
            apt.append(cnt)


print(len(apt))
apt.sort()

for i in apt:
    print(i)

