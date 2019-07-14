# 입력받은걸 아스키코드로 변환하는거 ord() 함수를 이용한다
# 아스키 코드를 문자로 바꾸는건 chr()을 사용한다


import sys

ascode = sys.stdin.readline().rstrip()

print(ord(ascode))
