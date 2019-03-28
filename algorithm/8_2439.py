a = int(input())

# for i in range(a):
#     print("{0:>a}".format("*"))
#
for i in range(a):
    print("{0}{1}".format(" "*(a-(i+1)),"*"*(i+1) ))