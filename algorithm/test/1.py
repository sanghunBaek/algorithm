
# zero, one, two, three, four, five, six, seven, eight, nine

def changeNum(number):
    if number == "0":
        return "zero"
    elif number == "1":
        return "one"
    elif number == "2":
        return "two"
    elif number == "3":
        return "three"
    elif number == "4":
        return "four"
    elif number == "5":
        return "five"
    elif number == "6":
        return "six"
    elif number =="7":
        return "seven"
    elif number == "8":
        return "eight"
    elif number == "9":
        return "nine"


def changeList(number):
    number = list(str(number))
    for i,j in enumerate(number):
       number[i] = changeNum(j)
    result = "".join(number)
    return result

# def againNum(number):
#     if number == "zero":
#         return "0"
#     elif number == "one":
#         return "1"
#     elif number == "two":
#         return "2"
#     elif number == "three":
#         return "3"
#     elif number == "four":
#         return "4"
#     elif number == "five":
#         return "5"
#     elif number == "six":
#         return "6"
#     elif number == "seven":
#         return "7"
#     elif number == "eight":
#         return "8"
#     elif number == "nine":
#         return "9"




# 입력이 numbers 에 저장된다
#ex ) # number =  [6, 1, 8]
def solution(numbers):
    answer = [] # 최종적으로 출력되는 순서
    value = []
    for i,j in enumerate(numbers):
        value.append((changeList(j),i))
    value.sort()

    for i in value:
        answer.append(numbers[i[1]])

    return answer


# number =  [6, 1, 8]
#
# print(solution(number))