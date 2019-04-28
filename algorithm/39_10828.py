import sys
num = int(sys.stdin.readline().rstrip())


class stack:
    def __init__(self):
        self.items = []
    def push(self,a):
        self.items.append(a)
    def pop(self):
        if not self.items:
            return -1
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if not self.items:
            return 1
        else:
            return 0
    def top(self):
        a = len(self.items)
        if a == 0:
            return -1
        return self.items[a-1]


# 이쪽에 일단 스택을 정의해야함
def commend_stack(value,a):
    value = value.split()
    if len(value) == 1:
        if value[0] == "pop":
            print(a.pop())
        elif value[0] == "top":
            print(a.top())
        elif value[0] == "size":
            print(a.size())
        else:
            print(a.isEmpty())
    else:
        a.push(int(value[1]))


a = stack()
for i in range(num):
    value = sys.stdin.readline().rstrip()
    commend_stack(value,a)
