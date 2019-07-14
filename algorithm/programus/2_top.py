


def checkLocation(a,heights):
    for i in range(len(heights)-1,-1,-1):
        if(heights[i] > a):
            return i+1
    return 0

def solution(heights):
    answer = [0] * len(heights)

    for i in range(len(heights)-1,0,-1):
        print(i)
        a = heights.pop()
        answer[i] = checkLocation(a,heights)
        print(answer)

    return answer

heights = [1,5,3,6,7,6,5]


print(solution(heights))