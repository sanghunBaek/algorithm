import sys

value = sys.stdin.readline().rstrip()
croalpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" ]
i = 0
total = 0

while i < len(value):
    if value[i:i+3] in croalpa:
        total = total + 1
        i = i + 3

    elif value[i:i+2] in croalpa:
        total = total + 1
        i = i + 2
    else:
        total = total + 1
        i = i + 1


print(total)
