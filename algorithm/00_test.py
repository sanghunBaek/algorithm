

inta = "2(3(hi)co)"
counts = inta.count("(")
calvalue = []


for i in range(counts*2):
    if inta.find("(") < inta.find(")") and inta.find("(") != -1:
        a = inta[ : inta.find("(")]
        inta = inta[inta.find("(")+1 :]
        calvalue.append(a)

    else:
        b = inta[ : inta.find(")")]
        inta = inta[inta.find(")")+1 :]
        calvalue.append(b)

# a  = int(inta[indexa-1])
# end = len(inta)
# b  = inta[indexa+1:end-1]
# print(a * b)








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