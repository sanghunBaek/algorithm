
#에라토스체네스의 체
#https://oneshottenkill.tistory.com/54

M,N = map(int,input().split())
num = [x for x in range(1, N+1)] #일단 구하고자하는 범위 끝 까지 배열만듬 (시작은 1부터)
num.insert(0,1) # 시작에다가 1을 넣어버림 그래서 인덱스범위를 맞춰주는거
for i in range(2,N+1):  # 2부터 시작해서 (1은 소수 아니니까) 소수의 배수들을 없애는 작업을 시작해줌
    j = 2 #자기자신 뺴야하니까 2부터 시작
    while N>=i*j: # 곱해진결과가 끝값보다 작은경우까지만 돌림
        num[i*j] = 1  # 나머지결과를 그냥 1로 만들어 버리는거
        j+=1
for l in num:
    if l!=1 and M<=l and l<=N:   # 나머지를 1로 만들어버림 쓸모없는것 그래서 여기서 조건을 1은 아니다 라고 줘버리니까 성공
        print(l)

#내가 만든 소수 구하는 함수
def isItSosu(num):
    count = 0
    if num == 1:
        return False
    end = int(math.sqrt(num)) # 이걸 통해서 제곱근값 이전까지만 for문 돌아가게 했음

    for i in range(1,end+1):
        if num % i == 0:
            count += 1
            if count > 1:
                return False
    return True