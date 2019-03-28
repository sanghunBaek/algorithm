N = int(input())


def countbag(N):
    total = []

    num = N // 3 + 1
    for i in range(num):
        for j in range(num):
            if i * 3 + j * 5 == N:
                total.append(i + j)

    if len(total) == 0:
        return -1
    else:
        return min(total)


print(countbag(N))
