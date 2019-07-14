a = input()
a = a.split(" ")

count1 = 0
count2 = 0

for i in range(len(a)):
    a[i] = int(a[i])

long = [1, 3, 5, 7, 8, 10, 12]
mid = [4, 6, 9, 11]
short = [2]

a[0] = a[0] - 1

while a[0] != 0:
    if a[0] in long:
        count1 = count1 + 31
    elif a[0] in mid:
        count1 = count1 + 30
    else:
        count1 = count1 + 28
    a[0] = a[0] - 1

count2 = a[1]
total = count1 + count2 - 1
result = total%7

if result == 1:
    print("TUE")
elif result == 2:
    print("WED")
elif result == 3:
    print("THU")
elif result == 4:
    print("FRI")
elif result == 5:
    print("SAT")
elif result == 6:
    print("SUN")
else:
    print("MON")





