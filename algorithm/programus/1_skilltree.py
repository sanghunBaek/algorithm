# 하나에서 실패가뜸 먼가 내가 생각하지 못한 문제가 있는거 같다 일단 넘어가요

from copy import copy

def func(x):
    if x == -1:
        return None
    else:
        return x

# a가 결국 스킬임
def checktrue(a):
    if -1 not in a:
        b = copy(a)
        a.sort()
        if a == b:
            return True
        else:
            return False

    c = a.index(-1)
    if a[c:].count(-1) == len(a[c:]):
        c = list(filter(func, a))
        d = copy(c)
        c.sort()

        # print(c)
        if len(c) == 0:  # 만약에 아무것도 포함안된거면 참이여야한다
            return True

        if c == d:
            return True
        else:
            return False
    else:
        return False

# print(checktrue([-1,0,1]))


def findlocation(skill,skill_trees):
    a = []
    for i in skill:
        a.append(skill_trees.find(i))
    return a


# print(checktrue(findlocation("abcd","ab")))


def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        if checktrue(findlocation(skill, i)):
            answer += 1

    return answer




skill = "CBD"
skill_trees = ["AKE", "AFS", "AES", "SFN"]

print(solution(skill,skill_trees))