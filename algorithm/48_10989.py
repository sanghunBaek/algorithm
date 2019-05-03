import sys
num = int(sys.stdin.readline())
result = []
for i in range(num):
    value = int(sys.stdin.readline())
    result.append(value)

def counting_sort(data):
    #입력받은 데이터가 어떠한 값으로 이루어 져있는지 확인
    indexs = set(data)
    indexs = list(indexs)
    indexs.sort()

    # 각각의 데이터의 개수를 파악
    count_num = []
    for i in indexs:
        count_num.append(data.count(i))
    # coutn
    # for i in data:
    #     count_num[index.index(i)] += 1
    # print(count_num)

    #데이터위치때문에 이렇게 하는거
    for i in range(1,len(count_num)):
        count_num[i] = count_num[i-1] + count_num[i]


    ordered_list = [0] * len(data)

    for i in data:
        # ind = index.index(i)
        # loc = count_num[ind]
        # ordered_list[loc-1] = i
        # count_num[ind] -= 1
        ordered_list[count_num[indexs.index(i)] - 1] = i
        count_num[indexs.index(i)] -= 1
    return ordered_list

result = counting_sort(result)

for i in range(len(result)):
    print(result[i])