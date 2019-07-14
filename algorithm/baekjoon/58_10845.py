import sys
count = int(sys.stdin.readline())

class que:
    def __init__(self):
        self.item = []
    def push(self,item):
        self.item.append(item)
    def pop(self):
        if len(self.item)==0:
            return -1
        else:
            return self.item.pop(0)
    def size(self):
        return len(self.item)
    def empty(self):
        if len(self.item) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.item) == 0:
            return -1
        else:
            return self.item[0]
    def back(self):
        if len(self.item) == 0:
            return -1
        else:
            return self.item[len(self.item)-1]


a = que()
for i in range(count):
    order = sys.stdin.readline().rstrip().split(" ")
    if order[0] == "push":
        a.push(int(order[1]))
    elif order[0] == "pop":
        print(a.pop())
    elif order[0] == "size":
        print(a.size())
    elif order[0] == "empty":
        print(a.empty())
    elif order[0] == "front":
        print(a.front())
    else:
        print(a.back())



