# print("{}".format("*"))
# 포매팅은 아닌거 같다 느낌이
# 문자를 더하기하는 방식으로 접근해 봐야겠다

# print("  *  ")
# print(" * * ")
# print("*****")
# a = "*"
# b = " "
# c = a + a + a + a
# print(c)

# 3을 받았다고 생각하고 만들어보자
# for문을 돌리는게 애매하네 .. 규칙이 안보여서



## 이건 그냥 위의 3개만 출력
# num = 3
# def makestar(num):
#     a = " "
#     b = "*"
#     c = []
#     c.append((num-1)*a + b + (num-1)*a)
#     c.append(a + b + a +b + a)
#     c.append(num//3 * 5 * b)
#     return c
#
# d = makestar(3)
# print(d)
# for i in d:
#     print(i)

# 흠 ... 일단 2번째까지 만들어보자

num = 6
def makestar2(num):
    a = " "
    b = "*"
    c = []
    c.append((num-1)*a + b + (num-1)*a)
    c.append(a*(num-2) + b + a + b + a*((num-2)))
    c.append(3*a*(num//3 - 1) +  5 * b +3*a*(num//3 - 1))
    return c

d = makestar2(num)
print(d)
for i in d:
    print(i)

