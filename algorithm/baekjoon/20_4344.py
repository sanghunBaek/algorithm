# 소수 출력하는거 소수점 부분
# float 형이면 %0.3f 머이런식으로해서 해결 가능하다
# 소수 3째자리까지 출력의 예시 %0.3f"% result[i]
# 배열이랑 sum 함수 쓸때 슬라이싱으로 일정부분만 합하는것도 가능하다

import sys

num = int(sys.stdin.readline().rstrip())
result =[]

for i in range(num):
    numlist = sys.stdin.readline().rstrip().split(" ")
    numlist = list(map(int, numlist))
    avg = sum(numlist[1:])/(len(numlist)-1)
    count = 0

    for j in range(1,len(numlist)):
        if numlist[j] > avg:
            count = count + 1

    percentage = count/(len(numlist)-1)*100
    result.append(percentage)

for i in range(len(result)):
    print("%0.3f"% result[i] + "%")