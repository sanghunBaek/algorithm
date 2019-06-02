import sys
inputvalue = list(map(int,sys.stdin.readline().rstrip().split(" ")))

a = dict()
def makegraph(num1,num2):
    a[num1] = {num2} | a[num1] if num1 in a else {num2}
    a[num2] = {num1} | a[num2] if num2 in a else {num1}

count = inputvalue[1]

for i in range(count):
    value = list(map(int, input().split(" ")))
    makegraph(value[0],value[1])


# dfs 만들기
def dfs(graph,start):
    visited = []
    vertex = [start,]

    while vertex:
        point = vertex.pop()
        if point not in visited:
            visited.append(point)#역순으로 추가해줘야지 작은걸 먼저 출력할것임 //이거 까지는 ok
            # 여기서 문제인게 만약에 그 포인트값의 그래프가 없다면? 오류가 나면서 문제가 발생함
            try:
                bb = list(graph[point] - set(visited))
                bb.sort(reverse=True)
                vertex.extend(bb)
            except:
                pass
            # bb = list(graph[point] - set(visited))
            # bb.sort(reverse = True)
            # vertex.extend(bb)
    return visited


# bfs 만들기
def bfs(graph,start):
    visited = []
    vertex = [start,]

    while vertex:
        point = vertex.pop(0)
        if point not in visited:
            visited.append(point)
            try:
                cc = list(graph[point] - set(visited))
                cc.sort()
                vertex.extend(cc)
            except:
                pass
    return visited



abcd = dfs(a,inputvalue[2])
efgh = bfs(a,inputvalue[2])

r=''
for s in abcd:
    r+=str(s)+' '
print(r.rstrip())


g=''
for s in efgh:
    g+=str(s)+' '
print(g.rstrip())


#
# for i in abcd:
#     print(i,end = " ")
#
# print("")
#
# for j in efgh:
#     print(j,end = " ")

# print(dfs(a,inputvalue[2]))
# print(bfs(a,inputvalue[2]))