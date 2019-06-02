import sys
count = int(sys.stdin.readline())
# result = []

def checkVPS(a):
    if a.count("(") != a.count(")"):
        return "NO"
    else:
        while len(a) != 0:
            if a.count(")") == 0 or a.count("(") == 0:
                return "NO"
            num1 = a.index(")")
            num2 = a.index("(")
            if num1 > num2:
                a.pop(num1)
                a.pop(num2)
            else:
                return "NO"
        return "YES"

for i in range(count):
    value = sys.stdin.readline().rstrip()
    value = list(value)
    print(checkVPS(value))
#아 이게 그냥 이렇게 정리해서 해줄필요가 없었구나
# for i in range(len(result)):
#     print(result[i])


