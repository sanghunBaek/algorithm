import sys
num = int(sys.stdin.readline().rstrip())

# def findson(num):
#     value = []
#     count = 1
#     while len(value) < num:
#         val = []
#         for i in range(1,count+1):
#             val.append(i)
#         if count%2 != 0 and count != 1:
#             val.reverse()
#         count = count + 1
#         value = value + val
#
#     return value[num-1]
#
# def parent(num):
#     value = []
#     count = 1
#     while len(value) < num:
#         val = []
#         for i in range(1,count+1):
#             val.append(i)
#         if count%2 == 0:
#             val.reverse()
#         count = count + 1
#         value = value + val
#
#     return value[num-1]

# print(str(findson(num)) + "/" + str(parent(num)))


def checkson(num):
    count = 1
    result = 0
    while num > result:
        result = result + count

        count = count + 1
    value = num - (result - (count - 1))
    a = [i for i in range(1,count)]
    if (count-1)%2 == 0:
        return a[value - 1]
    else:
        a.reverse()
        return a[value - 1]

def checkparent(num):
    count = 1
    result = 0
    while num > result:
        result = result + count

        count = count + 1
    value = num - (result - (count - 1))
    a = [i for i in range(1,count)]
    if (count-1)%2 == 0:
        a.reverse()
        return a[value - 1]
    else:
        return a[value - 1]

print(str(checkson(num)) + "/" + str(checkparent(num)))