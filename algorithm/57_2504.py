#내가 생각을 완전 잘못하고 있었음 일단 하는법은 알기는 했는데 답안도 없고 시도할 엄두가 안남 ㅎㅎ 일단 다르거 먼저 풀고 다시오자
# 개념은 이걸 확인 https://pangsblog.tistory.com/53

#이번에는 스택을 활용해서 풀어보자
#판별만을 우선 생각해보자



a = "[(())}"
a = list(a)

stack = []
result = 0
d = 0
# 2가지 경우가 생기면서 스택으로 풀기 어려워짐
for i in range(len(a)):
    stacklen = len(stack)

    if a[i] == "(":
        stack.append(2)
    elif a[i] == "[":
        stack.append(3)
    elif a[i] == ")" or a[i] == "]":
        c = stack.pop()
        d = len(stack)
    f = d #?? 이러면 무조건 같은거 아님??? ㅋㅋㅋ
    
    if f != d:
        result *= c
    else :
        result += c
print(result)







# 쉽게 생각하면 ( 이면 2 [이면 3을넣고 )이든 ]이든 나오면 그냥 pop 한다는느낌
# 아무래도 stack 의 길이를 가지고 할 수 있는듯 길이가 줄어들면 곱하는것 // 근데 줄었다고 어떻게 하는게 애매 애초에 pop하면 줄어서 더하기랑 곱을 어떻게 판별?
# 변수가 하나 더 있어야 할거같은데?
# 길이가 올라간다면?