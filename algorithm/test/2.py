
#판별식 펠리턴인지 아닌지
def checkF(value):
    a = list(value)
    a.reverse()
    a = "".join(a)
    if value == a:
        return True
    else:
        return False

def sumstr(a,b):
    str1 = "".join(b)
    return a+str1

# #출력값은 길이로 줘야한다
def solution(plain):
    answer = 0
    plain2 = list(plain)
    plain2.reverse()
    lenlist = [] # 여기다 가능성 있는거의 길이
    while plain2:
        sumSen = sumstr(plain,plain2)
        if checkF(sumSen):
            lenlist.append(len(sumSen))
        plain2.pop(0)
    answer = min(lenlist)

    return answer

# aaa = "abcde"
# print(solution(aaa))