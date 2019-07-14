import math

# 두개를 합쳐서 각 기능이 얼마만에 완성될수 있는지
def enddate(progresses,speeds):
    a = []
    for i in range(len(progresses)):
        a.append(math.ceil((100-progresses[i])/speeds[i]))
    return a

def solution(progresses, speeds):
    a = enddate(progresses,speeds)
    answer = []
    while(a):
        num = 0
        b = a.pop(0)
        while(len(a) != 0 and b >= a[0]):
            a.pop(0)
            num +=1
        answer.append(num+1)
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
# return = [2,1]

print(solution(progresses,speeds))

