# 문자식을 변형하는방법으로 풀었는데 이 전략이 잘 맞아떨어졌다 ㅎㅎ
# 중요한게 너무 어렵게 생각 않하는거랑 필요해 보이는거는 찾아보고 없으면 그냥 만들어서 써버리면 된다는것
import sys
number = int(sys.stdin.readline().rstrip())

def checkjisu(num):
    count = 0
    for i in range(10):
        if num % 2 == 0:
            num = num // 2
            count = count + 1
    return count


def result_of_star(num):
    k = ["  *  "," * * ", "*****"]
    countnum  = checkjisu(num/3)
    if num  == 3:
        return k
    else:
        for i in range(countnum):
            a  = " "
            # gup =  3 * i
            for j in range(len(k)):
                k.append(k[j] + a + k[j])

            for t in range(len(k)//2):
                k[t] = a * (len(k)//2) + k[t] + a * (len(k)//2)
        return k


result = result_of_star(number)
for i in range(len(result)):
    print(result[i])


