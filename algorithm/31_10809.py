# 파이썬 알파벳을 따로 지정해준게 있다
# import string
# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789

# find는 존재 x 면 -1출력해주고 index는 존재 x면 오류발생



import sys
import string

result = []
sentence = sys.stdin.readline().rstrip()
abclist = string.ascii_lowercase


for i in abclist:
    result.append(sentence.find(i))

for i in range(len(result)):
    print(result[i], end = " ")

