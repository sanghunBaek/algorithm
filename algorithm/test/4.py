
def findit(city,i,j):
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visit = [[0] * len(city[0]) for _ in range(len(city))]
    que = []
    que.append((i,j))
    while que:
        # 찾으면 끝내기
        x,y = que.pop(0)
        for k in direct:
            nx = x + k[0]
            ny = y + k[1]
            if nx < 0 or ny < 0 or nx >= len(city) or ny >= len(city[0]):
                continue
            if city[nx][ny] == 0:
                return visit[x][y] + 1
            else:
                visit[nx][ny] = 1 + visit[x][y]
                que.append((nx, ny))

# 주어지는것 그래프
def solution(city):
    for i in range(len(city)):
        for j in range(len(city[0])):
            if city[i][j] == 1:
                city[i][j] = findit(city, i, j)

    # answer = [[0,0,1],[1,1,2],[0,1,2]]
    return city