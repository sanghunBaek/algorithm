import sys

number  = int(sys.stdin.readline().rstrip())
result = []
def afcal(num,a):
    result = ""
    for i in a:
        result = result + i*num
    return result


for i in range(number):
    inputlist = sys.stdin.readline().rstrip().split(" ")
    result.append(afcal(int(inputlist[0]),inputlist[1]))

for i in range(len(result)):
    print(result[i])
