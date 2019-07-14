# 남자랑 여자회원수로 최대값 만들기  n ,m
import math
def maxteam(n,m):
    a = n//2
    if a > m:
        return m
    else:
        return a

# 최종적으로 최대를 구하기 위해서는 k에서 아까 구한거에서 남는거 뺴고
# 그걸 3으로 나누는 방식으로 생각해야함 즉 최대 수에서 이걸통해서 뺴내는식으로

def realTeam(n,m,k):
    a = maxteam(n,m)

    nam1 = n - 2*a
    nam2 = m - a
    # k = k - (nam1+nam2) # 여기서 문제가 있음 k에서 뺴면 안된다 k 가 더 작을 수 도 있는거임
    namSum = nam1 + nam2
    if namSum >= k:
        return a
    else:
        k = k - namSum
        b = math.ceil(k / 3)
        if a-b <0:
            return 0
        else:
            return a - b




a,b,c = map(int,input().split(" "))
print(realTeam(a,b,c))


