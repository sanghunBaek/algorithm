import sys
num = int(sys.stdin.readline())
wordList = []

for i in range(num):
    value = sys.stdin.readline().rstrip()
    wordList.append(value)

wordList = set(wordList)
wordList = list(wordList)
wordList.sort(key = lambda x:(len(x),x))

for i in range(len(wordList)):
    print(wordList[i])