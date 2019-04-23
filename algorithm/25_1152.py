# 문제가 쉽기는한데 좀 거지같다고 해야하나
# "  " 이게 반례였는데 아니 사람이 이런걸왜 추가하냐 ㅋㅋ
# 문장 넣는다면서 아무것도 안 넣어주는 경우까지 생각해야함?

import sys

sentence = sys.stdin.readline().strip()

splited = sentence.split(" ")
if splited[0] == "":
    print(0)
else:
    print(len(splited))
