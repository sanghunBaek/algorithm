#에라토스테네스의 채 소수를 가장 빠르게 판별해내는 알고리즘이라고한다
#https://primes.utm.edu/glossary/page.php?sort=SieveOfEratosthenes


M,N = map(int,input().split())
num = [x for x in range(1, N+1)]
num.insert(0,1)
for i in range(2,N+1):
    j = 2
    while N>=i*j:
        num[i*j] = 1
        j+=1
for l in num:
    if l!=1 and M<=l and l<=N:
        print(l)


























# def makeBesu(num,end):
#     besuLS = []
#     gop = 2
#     a = num * gop
#     while a <= end:
#         besuLS.append(a)
#         gop += 1
#         a = num * gop
#     return set(besuLS)
#
# def isItSosu(num):
#     count = 0
#     if num == 1:
#         return False
#
#     for i in range(1,num):# 더 빠르게 판별 못하나?
#         if num % i == 0:
#             count += 1
#             if count > 1:
#                 return False
#     return True
#     # if count == 1:
#     #     return True
#
# #흠 .. set은 순서가 없다는게 단점
# # 차라리 for문 말고 while 써야할거 같은데 조건을 어떻게 줘야하지?
#
# valueLS = [i for i in range(number[0],number[1]+1)]  #### 이거를
# # for i in range(number[0],number[1]+1):
# #     valueLS.append(i)
# print(len(valueLS))
#
# i = 0
# while i < len(valueLS):  # 이거 먼가 수정필요해보인다 처음에 5만이였으면 5만번을 반복해줘야한다는 문제가 있음 무조건? 아닌듯 바귀면 수정되는긋
#     num = valueLS[i]
#     print("len값 바뀌는거?",len(valueLS))
#     print(num)
#     print("i값",i)
#     if num == 1:
#         i += 1
#         pass
#         # i += 1
#     elif isItSosu(num):
#         valueLS = set(valueLS)
#         valueLS = valueLS - makeBesu(num, number[1])
#         i += 1
#         valueLS = list(valueLS)
#         # print(num)
#         print("배수1", makeBesu(num, number[1]))
#         print("과정1", valueLS)
#     else:
#         valueLS = set(valueLS)
#         valueLS = valueLS - makeBesu(num,number[1])
#         # i += 1
#         valueLS = list(valueLS)
#         valueLS.pop(i)
#
#         # print(num)
#         print("배수2",makeBesu(num,number[1]))
#         print("과정2", valueLS)
#
# valueLS.sort()
#
# for i in range(len(valueLS)):
#     print(valueLS[i])
