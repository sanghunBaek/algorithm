# n종류의 동전
# 그 가치의 합 k로 만드려함
# 필요한 동전 개수의 최소값
# n = 동전의 종류 // 작은순으로 주어진다
# k = 총합
#
# 주어지는 n을 리스트에 저장?
# 뒤에서 부터 나눠보는거 어떰?
# 나눠지는지
# 몫이 있어야함

n, k = map(int, input().split(" "))


coin = []
for i in range(n):
    value = int(input())
    coin.append(value)

coin.sort(reverse = True)
totalcnt = 0

for i in range(len(coin)):
    if k == 0:
        break
    else:
        if k // coin[i] !=0 :
            mok = k // coin[i]
            totalcnt += mok
            k = k % coin[i]
print(totalcnt)


