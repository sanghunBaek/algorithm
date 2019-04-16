# 파이썬 기본으로 평균을 구하는 함수는 없는듯 그냥 다 합하고 나눠줘야함
# numpy인가 그거 쓰라는데

import sys

num = int(sys.stdin.readline().rstrip())
score = sys.stdin.readline().rstrip().split(" ")
score = list(map(int, score))
maxnum = max(score)


for i in range(len(score)):
    score[i] = score[i]/maxnum*100

print(sum(score)/len(score))