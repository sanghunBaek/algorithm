a = "Mississipi"
a = a.upper()
result = []
charlist = []
b = set(a)

for i in b:
    result.append(a.count(i))
    charlist.append(i)

print(charlist)
print(result)

for i in range(1,len(result)):
    a = 0
    count = 0
    if result[i] > result[i-1]:
        a = i
        count = count + 1
