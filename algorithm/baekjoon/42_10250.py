import sys
num = int(sys.stdin.readline().rstrip())
result = []

def testfunction(test):
    count = 0
    while 1:
        for i in range(1, test[1] + 1):
            for j in range(1, test[0] + 1):
                if i >= 10:
                    result = str(j) + str(i)
                    count = count + 1

                    if count == test[2]:
                        return result
                else:
                    result = str(j) + "0" + str(i)
                    count = count + 1

                    if count == test[2]:
                        return result


for i in range(num):
    test = sys.stdin.readline().rstrip().split(" ")
    test = list(map(int,test))
    result.append(testfunction(test))


for i in range(len(result)):
    print(result[i])

