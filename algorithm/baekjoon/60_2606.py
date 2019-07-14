import sys
countCom = int(sys.stdin.readline())
connectLine = int(sys.stdin.readline())

a = dict()
def makegraph(num1,num2):
    a[num1] = {num2} | a[num1] if num1 in a else {num2}
    a[num2] = {num1} | a[num2] if num2 in a else {num1}

def bfs(graph):
    visited = []
    quelist =[1,]
    while quelist:
        vertex = quelist.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            try:
                quelist.extend(graph[vertex] - set(visited))
            except:
                pass
    return visited

for i in range(connectLine):
    value = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    makegraph(value[0],value[1])

print(len(bfs(a))-1)