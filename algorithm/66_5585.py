# 1000엔짜리 지페
#
# 500
# 100
# 50
# 10
# 1

# 1000 - x 할거임
# 남은 수
# 나눠보는거 최소로


# 무조건 제일 큰거부터 한다고 좋은거 아님
#

value = int(input())
a = 1000 - value
b = [500,100,50,10,5,1]
def cnting(a):
    cnt = 0
    for i in b:
        if a//i != 0:
            c = a//i
            a = a%i
            cnt += c
    return cnt
print(cnting(a))