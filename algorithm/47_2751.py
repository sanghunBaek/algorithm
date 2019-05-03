# 이게 병렬 힙 정렬 머시기 하는데
# 파이썬은 그냥 sort로 끝내버려서
# 숫자 받는거 그냥 rstrip() 안써줘도 ㄱㅊ


import sys
num = int(sys.stdin.readline().rstrip())
result = []
for i in range(num):
    value = int(sys.stdin.readline().rstrip())
    result.append(value)

result.sort()
for i in range(len(result)):
    print(result[i])


