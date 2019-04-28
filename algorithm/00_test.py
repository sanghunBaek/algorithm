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

a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*",end = "")
    print("")