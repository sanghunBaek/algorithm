
# 이번문제의 핵심을 정리하자면
# 1. 방향을 지정하고 각 꼭지점에서 전체로 이동해야한다
# 2. 각 점 별로 새롭게 배열을만들어줘서 그것별로 따로 측정을 해서 cnt를 구해준다
# 3. 그리고 기존에 존재하는거랑 비교해서 큰거를 뽑아낸다
# 4. 큐를 통해서 했기 때문에 즉 bfs로 풀었기 때문에 마지막에 남는 x y 가 제일 긴 점이 되는거다 한줄씩 가니까 제일 마지막까지
# 진행되던게 최장 길이

# 특별하게 알아야되는 지식은 없었다.
#... 후 y를 x 로 쓴거를 확인못해서 진짜 개오래.. 걸렸음 시발것
import sys

def bfs(board,m,n):
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    max_cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'L':
                visit = [[0] * n for _ in range(m)]
                q = []
                q.append((i, j))

                while q:
                    x, y = q.pop(0)
                    for dx,dy in direct:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n:
                            continue
                        if board[nx][ny] == 'L' and visit[nx][ny] == 0:
                            visit[nx][ny] = 1 + visit[x][y]
                            q.append((nx, ny))

                max_cnt = max(max_cnt, visit[x][y])
    print(max_cnt)

# m, n = map(int,sys.stdin.readline().rstrip().split(" "))
m, n = map(int, input().split())
board =[]
for i in range(m):
    # graph.append(list(sys.stdin.readline().rstrip()))
    board.append(input())


bfs(board,m,n)

