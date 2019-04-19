import sys

end_num = int(sys.stdin.readline().rstrip())

def check_hansu(end_num):
    total = 0
    for i in range(1, end_num+1):
        if i < 10:
            total = total + 1
        elif i >= 10 and i < 100:
            total = total + 1
        elif i >= 100 and i < 1000:
            b = [int(j) for j in str(i)]
            if (b[1] - b[0]) == (b[2] - b[1]):
                total = total + 1

    return total

print(check_hansu(end_num))
