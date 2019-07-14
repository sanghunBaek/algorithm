# 그냥 쭉 카운팅하는게 어떨까? 규칙을 찾으려고 했는데 규칙은 정말 안나옴
# 하나씩 올리고 그때 비교하고 그러면서 카운팅하는식으로?
# 리미트 두고

# 음 일단 답은 나오는데 시간초과임 .. 어떻게 해야하지
# 일단 예상가는 원인은 값이 아닌거를 너무 늦게 찾아내서? 일단 지금은 일일이 확인하는 식이니까
# 다른 규칙이 있나 내가 모르는?

# 1씩 더하는거는 너무 계산이 많아진다고함

# import sys
#
# loopnum = int(sys.stdin.readline().rstrip())
# result = []
#
# def checkit(m,n,k,z):
#     x = 1
#     y = 1
#     count = 1
#
#
#     while 1:
#         if x == m and y == n:
#             return -1
#         if k == x and z == y:
#             return count
#
#         if x + 1 > m:
#             x = 1
#         else:
#             x = x + 1
#
#         if y + 1 > n:
#             y = 1
#         else:
#             y = y + 1
#
#         count = count + 1
#
# for i in range(loopnum):
#     num = sys.stdin.readline().rstrip().split(" ")
#     num = list(map(int, num))
#     result.append(checkit(num[0],num[1],num[2],num[3]))
#
# for i in range(len(result)):
#     print(result[i])



# 이것도 시간초과나면 멀 어쩌라는거지 .. ㅅㅂ

import sys
count = int(sys.stdin.readline().rstrip())

#이거는 m < n 일때
def makelist(num,fin,n,inter):
    count = 1
    b = num

    if abs(b - fin)%abs(inter) != 0:
        return -1

    while b !=fin:
        b = b + inter
        if b <= 0:
            b = b + n
        # a.append(b)
        count = count + 1
        # if b == num: #같은게 나오기 하나 전인데??? 맞는거 같다 시작점이 같아지는거니까 이전거에서 12로 끝나버렸으면 그다음 1이면서 같아짐
        #     return -1
    # return a
    return count

# print((len(makelist(3,9,12,inter)) - 1 )*(m) + 3) # 이거는 m이 n보다 작은경우에서 성립 +해준건 결국 num을 더해주는거

#보니까 여기서 문제 있음 b를 구하는과정서 m이랑 n이랑 차이가 존나 나면 안된다 큰수가 문제야 ...
# 참고 https://www.acmicpc.net/board/view/21503
def makelist2(num,fin,n,inter):
    count = 1
    if num > n:
        num  = num - n
    # a = [num]
    b = num
    if abs(b - fin)%abs(inter) != 0:
        return -1

    while b != fin:
        b = b + inter
        if b > n:
            b = b - n
        # a.append(b)
        count = count + 1
        # if b == num:
        #     return -1
    # return a
    return count

# print(  (len(makelist2(10,4,8,2)) -1)*(10) + 10 )


def final(m,n,num,fin):
    inter = m - n
    if m < n:
        if makelist(num,fin,n,inter) == -1:
            return -1
        else:
            # return (len(makelist(num,fin,n,inter)) - 1)*m + num
            return (makelist(num, fin, n, inter) - 1) * m + num
    elif m > n:
        if makelist2(num,fin,n,inter) == -1:
            return -1
        else:
            # return (len(makelist2(num,fin,n,inter)) - 1) * m + num
            return (makelist2(num, fin, n, inter) - 1) * m + num
    else:
        if num != fin:
            return -1
        else:
            return num


# print(final(13,11,5,6))
result = []
for i in range(count):
    sen = sys.stdin.readline().rstrip().split(" ")
    sen = list(map(int,sen))
    result.append(final(sen[0],sen[1],sen[2],sen[3]))

for i in range(len(result)):
    print(result[i])