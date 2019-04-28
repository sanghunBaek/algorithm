# 스택이라는게 결국 LIFO의 개념만 잘 지키면 되는것
# append() 랑 pop를 잘 사용하는것

# class 를 통해서 만들어진 스택은 다음과 같다.
class stack:
    def __init__(self):
        self.items = []  # 선언과 동시에 자동으로 이거 만들어줌
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return not self.items # 만약에 비어있으면 fall이니까 여기서 빈 스택은 true를 출력하는거

#활용
a = stack()
a.push(2)
a.push(3)
print(a.items)
print(a.pop())