# 일단 만들어볼까 ?


# n을 넣었을때 차례로 증가할 수 있도록


# 3으로 나눠야함
# 나누는걸 기준으로해서 값을 구해야함
# 3으로 나눠서 나머지 랑 몫으로 나누고
# 나머지는 배열에 인덱스로
# 다음꺼 구해서 인덱스로
# 이런식으로해서 더하는식
def changeOTF(n):
    result = ""
    value = [1,2,4]
    if((n-1)//3 == 0):
        return str(value[n-1])

    while(n//3 != 0):
        m = n%3
        n = n//3
        result = str(value[m-1]) + result

    return str(value[n-1]) + result

print(changeOTF(10))


