
a = input()
a = a.split(" ")

for i in range(len(a)):
    a[i] = int(a[i])

print((a[0]+a[1])%a[2])
print((a[0]%a[2] + a[1]%a[2])%a[2])
print((a[0]*a[1])%a[2])
print((a[0]%a[2] * a[1]%a[2])%a[2])

