
#그래프 만드는것
#이걸 미리 앞에  a = dict() 같이 딕셔너리 지정하면 쓸수 있음 근데 global 안해주고 어떻게 가능한거지? 변수는  global 해줘야지 쓸 수 있음
def makegraph(num1,num2):
    a[num1] = {num2} | a[num1] if num1 in a else {num2}
    a[num2] = {num1} | a[num2] if num2 in a else {num1}
    # if num1 in a:
    #     a[num1] |= {num2}  # set은 더하려면 저렇게 해줘야함
    # else:
    #     a[num1] = {num2}
    #
    # if num2 in a:
    #     a[num2] |= {num1}
    # else:
    #     a[num2] = {num1}


# 그래프는 이런식으로 저장된다
graph = {'1': set(['2', '3', "4"]),
         '2': set(['1', '4']),
         '3': set(['1', '4']),
         '4': set(['1','2','3']),
         }

# 둘의 가장 큰 창이점은 DFS는 결국 stack 이라서 들어간게 남중에나오는 방식
# BFS는 쿠라서 먼저들어간게 먼저나옴
# 그게 가장 큰 차이이자 핵심 나머지 코드는 다 비슷함


# 깊이 우선탐색 그냥 밑으로 쭉 내려가 버리는 방식
# 모든 노드를 방문 하고자 하는 경우에 이 방법을 선택
def dfs(graph, root):  # 그래프랑 시작점을 설정해준다
    visited = []  # 각 꼭짓점(vertex)이 방문되었는지 기록
    stack = [root, ]

    while stack:  # stack 이 비게 되면 탐색 끝  // 빈다는게 전체 다 돌아야한나든 ㄴ의미
        vertex = stack.pop()  # 방문되어지고 있는 꼭짓점
        if vertex not in visited:  # 꼭지점이 방문된경우가 아닌경우
            visited.append(vertex) # 방문된것에 추가
            stack.extend(graph[vertex] - set(visited)) # 해당 꼭지점에서 갈 수 있는곳에서 방문한곳을 제외한것을 추가해준다

    return visited;

print(dfs(graph,"1"))

# 넓이 우선 탐색은 같은 라인먼저 다하고 다음라인으로 내려가는 방법
# 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때

def bfs(graph, root):
    visited = []  # 방문한 곳을 기록
    queue = [root]  # 큐에 시작점을 줄세움

    while queue:  # queue 가 빌 때 까지 탐색을 계속
        vertex = queue.pop(0)  # 큐의 맨 앞의 원소를 방문할 꼭짓점으로 설정

        if vertex not in visited:  # 꼭짓점이 방문된 적이 없다면 방문 기록에 추가
            visited.append(vertex) # 이렇게 for문 쓸필요 없음 위에처럼 그냥 set으로 - 해주는 방법있음
            for node in graph[vertex]:  # 꼭짓점에 연결된 노드들 중, 그냥 for문을 돌려버림
                if node not in visited:  # 방문 안 된 곳 만을
                    queue.append(node)  # 큐에 줄세움

    return visited



#https://blog.ilkyu.kr/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B9%8A%EC%9D%B4-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89Depth-First-Search%EA%B3%BC-%EA%B5%AC%ED%98%84-%EB%B0%A9%EB%B2%95
#https://blog.ilkyu.kr/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89Breadth-First-Search%EA%B3%BC-%EA%B5%AC%ED%98%84-%EB%B0%A9%EB%B2%95
