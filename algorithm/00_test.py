import sys

N = int(input())

dic = {}

for i in range(N):
    a = int(sys.stdin.readline())

    if a in dic:
        dic[a] = dic[a] + 1

    else:
        dic[a] = 1

for sorted in sorted(dic.items()):
    for i in range(sorted[1]):
        print(sorted[0])



# find의 두번째인수는 시작점 세번쨰인수는 끝점 (검색하는 범위를 지정하는거임 )
# 문제 풀때 필요한기능이 내 상식선 + 검색결과 안나온다면 그냥 내가 직접 구현하는게 답일 수 있다. (생각보다 얼마 안걸림)

# inta = "2(3(hi)co)x2(ko)"
# counts = inta.count("(")
#
# def replace(start,end,text1,text2):
#     a = text1[:start]
#     b = text1[start:end+1]
#     c = text1[end+1:]
#     return a + text2 + c
#
# def findit(text):
#     for i in range(text.count("(")):
#         a = text.find(")")
#         b = []
#         j = 0
#         print(a)
#         for i in range(a):
#             if text.find("(", j,a) != -1:
#                 b.append(text.find("(", j))
#                 j = b[i] + 1
#         print(b)
#         c = b.pop()
#         sumt = text[c + 1:a] * int(text[c - 1])
#         text = replace(c - 1, a, text, sumt)
#         print(text)
#
#
# findit(inta)




#
# bakery_schedule = ["12:00 10"]
# current_time = "12:00"
# K = 11
#
# def solution(bakery_schedule,current_time,K):
#     hourmin = []
#     count = []
#
#     somelist = []
#     for i in range(len(bakery_schedule)):
#         b = bakery_schedule[i].split(" ")
#         hourmin.append(b[0])
#         count.append(int(b[1]))
#
#     for i in range(len(hourmin)):
#         c = list(map(int, hourmin[i].split(":")))
#         d = list(map(int, current_time.split(":")))  # 이게 입력값
#
#         if c[0] < d[0]:
#             somelist.append(1)
#         elif c[0] == d[0]:
#             if c[1] - d[1] < 0:
#                 somelist.append(1)
#             else:
#                 somelist.append(0)
#         else:
#             somelist.append(0)
#
#     # print(hourmin)
#     # print(count)
#     # print(somelist)
#     thispoint = somelist.index(0)
#     # print(thispoint)
#     totalbk = 0
#
#     while totalbk < K:
#         if thispoint > len(count)-1:
#             return -1
#         totalbk = totalbk + count[thispoint]
#         thispoint = thispoint + 1
#
#
#     finalindex = thispoint - 1
#     ps = bakery_schedule[finalindex].split(" ")
#
#     aab = list(map(int, ps[0].split(":")))
#     # print(aab)
#     # print(d)
#
#     finalresult = 0
#
#     if d[1] > aab[1]:
#         finalresult = (aab[0] - d[0] - 1) * 60 + (60 - (d[1] - aab[1]))
#     else:
#         finalresult = (aab[0] - d[0]) * 60 + (aab[1] - d[1])
#     return finalresult
#
# print(solution(bakery_schedule,current_time,K))





# bakery_schedule = ["12:00 10"]
# current_time = "12:00"
# K = 11
# hourmin =[]
# count = []
#
# somelist = []
# for i in range(len(bakery_schedule)):
#     b = bakery_schedule[i].split(" ")
#     hourmin.append(b[0])
#     count.append(int(b[1]))
#
#
# for i in range(len(hourmin)):
#     c = list(map(int,hourmin[i].split(":")))
#     d = list(map(int,current_time.split(":"))) #이게 입력값
#
#     if c[0] < d[0]:
#         somelist.append(1)
#     elif c[0] == d[0]:
#         if c[1] - d[1] < 0:
#             somelist.append(1)
#         else:
#             somelist.append(0)
#     else:
#         somelist.append(0)
#
# # print(hourmin)
# # print(count)
# # print(somelist)
# thispoint = somelist.index(0)
# # print(thispoint)
# totalbk = 0
# while totalbk < K:
#     totalbk = totalbk + count[thispoint]
#     thispoint = thispoint + 1
#
#
# finalindex = thispoint - 1
# ps = bakery_schedule[finalindex].split(" ")
#
# aab = list(map(int,ps[0].split(":")))
# # print(aab)
# # print(d)
#
# finalresult = 0
#
# if d[1] > aab[1]:
#     finalresult = (aab[0]-d[0]-1)*60 + (60 -(d[1]-aab[1]))
# else:
#     finalresult = (aab[0] - d[0])*60 + (aab[1]-d[1])
# print(finalresult)
#
#
#
#





###### 11번가 데모 버전 1번 ######
# v = [[1, 4], [3, 4], [3, 10]]
#
# def solution(v):
#     answer = []
#     xvalue = []
#     yvalue = []
#     for i in range(3):
#         xvalue.append(v[i][0])
#         yvalue.append(v[i][1])
#     xset = set(xvalue)
#     yset = set(yvalue)
#     for j in xset:
#         if xvalue.count(j) == 1:
#             answer.append(j)
#     for k in yset:
#         if yvalue.count(k) == 1:
#             answer.append(k)
#
#     return answer
# solution(v)


###### 11번가 데모 버전 2번 ######
# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     for j in range(a):
#         print("*",end = "")
#     print("")