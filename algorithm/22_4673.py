# 먼지는 정확하게 모르겠는데 파이썬에서는 리스트 안에 for문을 통해서 값 생성할 수 있음
# [str(x) for x in range(1,10)] 이런식으로 앞에 있는 값으로 for문의 결과를 줘서 출력하는 방식으로 리스트 만들어주기 가능
# 그래서 입력받은 숫자의 각자리 수를 출력해야하는 경우에 그 숫자를 문자형으로 만들고 저런방식으로
# [int(i) for i in str(num)] 이렇게 만들어줄 수 있다

def calculater(num):
    b = [int(i) for i in str(num)]
    c = num + sum(b)
    return c

list = []
for i in range(1,10001):
    list.append(calculater(i))

for i in range(1,10001):
    if i not in list:
        print(i)





