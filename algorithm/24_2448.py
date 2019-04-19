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

num = 3
def makestar2(num):
    a = " "
    b = "*"
    c = []
    c.append((num-1)*a + b + (num-1)*a)
    c.append(a*(num-2) + b + a + b + a*((num-2)))
    c.append(3*a*(num//3 - 1) +  5 * b +3*a*(num//3 - 1))
    return c

d = makestar2(3)
# print(d)
# for i in d:
#     print(i)
#

f = makestar2(3)

k = makestar2(6)

# for i in k:
#     print(i)
# for i in range(len(d)):
#     print(d[i] + " " + f[i])
# sixstar = []

for i in range(len(d)):
    k.append(d[i] + " " + f[i])

# for i in k:
#     print(i)

for i in range(12):
    a = " "
    if i < 6:
        print(a * 6 + k[i])
    else:
        print(k[i-6] + a + k[i-6])

def semistar():
    return


def finalstar(num):
    a = " "
    if i < num/2:
        print(a * 6 + finalstar(num/2))
    else:
        print(finalstar(num/2) + a + finalstar(num/2))

# 이런식으로 재귀함수로 문제를 풀어야할것 같다
# 24를 구하라고하면 12 그리고 6 그리고 3에서 이제 제대로 시작할 수 있게끔
