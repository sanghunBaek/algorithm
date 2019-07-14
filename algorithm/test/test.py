

s = "3people unFollowed me"


def checkword(s):
    s = s.lower()
    s = s.replace(s[0], s[0].upper(), 1)
    return s


def splitsen(s):
    a = s.split(" ")
    for index, i in enumerate(a):
        a[index] = checkword(i)
    return " ".join(a)


def solution(s):
    s.lower()
    i = s.split(" ")
    for j in i:
         = j.capitalize()

    answer = ' '.join(i)
    return answer

print(solution(s))