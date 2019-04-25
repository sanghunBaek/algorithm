#좀 더럽게 풀었음 리스트로하면 깔끔하게 풀수 있다
import sys
sentence = sys.stdin.readline().rstrip()
count = 0

for i in sentence:
    if i in "ABC":
        count = count + 3
    elif i in "DEF":
        count = count + 4
    elif i in "GHI":
        count = count + 5
    elif i in "JKL":
        count = count + 6
    elif i in "MNO":
        count = count + 7
    elif i in "PQRS":
        count = count + 8
    elif i in "TUV":
        count = count + 9
    elif i in "WXYZ":
        count = count + 10
    else:
        count =  count + 11

print(count)