# 입력받는것 배열로 저장 안하고 출력하는게 중요함
# 메모리는 기본적으로 8mb? 만 주기 때문에 저장하면 바로 초과난다고 함

# 하 참  딕셔너리로 한거는 왜 안되는거지?
import sys
N = int(input())
series = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    series[a] = series[a] + 1

for b in range(len(series)):
    if series[b] !=0:
        for c in range(series[b]):
            print(b)


# import sys
# num = int(sys.stdin.readline())
#
# indexlist = []
# valuelist = []
#
# for i in range(num):
#     value = int(sys.stdin.readline())
#     if value in indexlist:
#         valuelist[indexlist.index(value)] += 1
#     else:
#         indexlist.append(value)
#         valuelist.append(1)
#
# print(indexlist)
# print(valuelist)

# for j in range(len(indexlist)):
#     a = min(indexlist)
#     c = indexlist.index(a)
#     b = valuelist[c]
#     for k in range(b):
#         print(a)
#     indexlist.remove(a)
#     valuelist.pop(c)

# print(indexlist)
# print(valuelist)




# 딕셔너리 활용해봤는데 시간초과로 안된다 그냥 2차원 리스트로 생각해보자
import sys
# num = int(sys.stdin.readline())
num = int(input())
diclist = {}

# def makeinxt(num):
#     if num in diclist:
#         diclist[num] += 1
#     else:
#         diclist[num] = 1

for i in range(num):
    value = int(sys.stdin.readline())
    if value in diclist:
        # diclist[value] += 1
        diclist[value] = diclist[value] + 1
    else:
        diclist[value] = 1

for i in sorted(diclist.items()):
    for j in range(i[1]):
        print(i[0])

# for i,j in diclist:
#         for k in range(j): sys.stdout.write(str(i)+'\n')

# for i in indexlist:
#     for j in range(diclist[i]): sys.stdout.write(str(i)+'\n')
    # for j in range(diclist[i]):
    #     print(i)







# 기존의 입력값 배열로 저장해서 메모리초과뜬거
# def counting_sort(data):
#     #입력받은 데이터가 어떠한 값으로 이루어 져있는지 확인
#     indexs = set(data)
#     indexs = list(indexs)
#     indexs.sort()
#
#     # 각각의 데이터의 개수를 파악
#     count_num = []
#     for i in indexs:
#         count_num.append(data.count(i))
#     # coutn
#     # for i in data:
#     #     count_num[index.index(i)] += 1
#     # print(count_num)
#
#     #데이터위치때문에 이렇게 하는거
#     for i in range(1,len(count_num)):
#         count_num[i] = count_num[i-1] + count_num[i]
#
#
#     ordered_list = [0] * len(data)
#
#     for i in data:
#         # ind = index.index(i)
#         # loc = count_num[ind]
#         # ordered_list[loc-1] = i
#         # count_num[ind] -= 1
#         ordered_list[count_num[indexs.index(i)] - 1] = i
#         count_num[indexs.index(i)] -= 1
#     return ordered_list
#
# result = counting_sort(result)
#
# for i in range(len(result)):
#     print(result[i])