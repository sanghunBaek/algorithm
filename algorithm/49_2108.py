# 산술평균
# 중앙값
# 최빈값
# 범위

# 입력을 배열로 안받는다고 생각해보자


#시간초과 뜸

import sys
count = int(sys.stdin.readline())
a = []
for i in range(count):
    value = int(sys.stdin.readline())
    a.append(value)

# a = [-1,5,2,3,-7,10,3,2]
print("산술평균 : ", round(sum(a)/len(a)))

a.sort()
mid = len(a)//2
print("중앙값 :", a[mid])


# 라스트 최빈값
b = set(a)
freList = []
indexList =[]
for i in b:
    indexList.append(i)
    freList.append(a.count(i))

c = max(freList)
d = freList.count(c)
f = []

if d != 1:
    e = 0
    for i in range(d):
        ind = freList.index(c,e)
        f.append(ind)
        e = ind + 1
    g = []
    for j in f:
        g.append(indexList[j])
    aa = min(g)
    g.remove(aa)
    bb = min(g)
    print("최빈값 : ", bb)

else:
    print("최빈값 : ", indexList[freList.index(c)])

#범위
print("범위 :", a[len(a)-1] - a[0])




# def avgFunc(a):
#     return round(sum(a)/len(a))
# def
#
# # 입력을 맞춰주는거
# def makeIn(num):
#     return num + 4000
#
# #출력을 맞춰주는거
# def makePri(num):
#     return num = num - 4000
#
#
# listOfValue = [0]*8001
# for i in range(count):
#     value = int(sys.stdin.readline())
#     listOfValue[makeIn(value)] += 1

