#문자를 하나하나씩 다 끊어서 하려면 그냥 문자를 list로 만들어주면 된다
# a.sort(reverse=True) 하면 내림차순 정렬
# join(b) 를 쓴다면 저기 b는 문자형태 리스트 여야함

import sys
a = sys.stdin.readline().rstrip()
b = list(a)
b = list(map(int,b))
b.sort(reverse = True)
b = list(map(str,b))
c = "".join(b)
print(c)
