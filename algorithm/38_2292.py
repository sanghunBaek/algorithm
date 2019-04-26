# 문제를 처음에는 배열로 다만들고 거기에 속하는걸로 찾았는데 그러면 시간초과가 나왔음
# 이 후에는 그냥 < > 등 부등호를 통해서 만 계산되도록함
# 그리고 나서는 이제 규칙을 적용할때 첫 배열과 나머지에서 차이가 조금있어서 if로 상황 나눠서 풀었음

import sys
num = int(sys.stdin.readline().rstrip())

def countwall(num):
    b = []
    start = 1
    count = 1
    end = 1
    while not((num >= start) and (num <= end)):
        if count == 1:
            start = 1
            end = 7
            count = count + 1

        else:
            start = end + 1
            end = start + 6*(count) - 1
            count = count + 1

    return count

print(countwall(num))


# def countwall(num):
#     b = []
#     start = 1
#     count = 1
#     end = 1
#     while num not in b:
#         if num == 1:
#             break
#         start = end
#         end = start + 6*(count)
#         b = [i for i in range(start+1, end+1)]
#         count = count + 1
#
#     return count
#
# print(countwall(num))

