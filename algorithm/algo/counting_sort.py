# 계수정렬 이라고도 한다
# 시간복잡도가 O(n+k)로 엄청 낮다고함 n은 정렬할 숫자의 개수 , k는 정렬할 숫자중 가장 큰값
# k 값에 따라 Best case랑 Worst case가 극과극으로 갈린다고 한다
# 저 큰수가 졸라 크면 별로 안좋아진다는 뜻  (큰 수에 영향을 많이 받는 정렬이다)

# 기본개념 :
# x보다 작은 원소의 개수가 N개일 떄 , X는 N+1번째에 위치해야 한다.
# 전체 숫자를 스캔한 후 출현 빈도를 기준으로 정렬한다는 의미 // 즉 숫자의 범위가 너무 광범위하거나 예측하기 힘들때는 사용하기 안좋음

# enumerate
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.

# ex)
# >>> t = [1, 5, 7, 33, 39, 52]
# >>> for p in enumerate(t):
# ...     print(p)
# ...
# (0, 1)
# (1, 5)
# (2, 7)
# (3, 33)
# (4, 39)
# (5, 52)

#https://m.blog.naver.com/PostView.nhn?blogId=itperson&logNo=220846813778&proxyReferer=https%3A%2F%2Fwww.google.com%2F
# def counting_sort(data):
#     MAX_NUM = max(data) + 1
#     count_list  = [0] * (MAX_NUM)
#
#     for num in data:
#         count_list[num] += 1
#
#     index = 0
#
#     for num,count in enumerate(count_list):
#         for repeat in range(count):
#             data[index] = num
#             index += 1
#     return data
#
#
# data = [2,3,5,1,2,1,1]
# print(counting_sort(data))


# 왜 틀렸는지 알겠음
# 이게 보니까 블로그에서 준거는 전체 배열을 다 만들어야되는데 그러면 비효율적인거임
# 지정되는것만 딱 나오도록 만들어야한다

#https://bowbowbow.tistory.com/8 이해는 완벽

def counting_sort(data):
    #입력받은 데이터가 어떠한 값으로 이루어 져있는지 확인
    index = set(data)
    index = list(index)
    index.sort()

    print(index)
    #각각의 데이터의 개수를 파악
    count_num = []
    for i in index:
        count_num.append(data.count(i))
    print(count_num)
    #데이터위치때문에 이렇게 하는거
    for i in range(1,len(count_num)):
        count_num[i] = count_num[i-1]+count_num[i]
    print(count_num)

    ordered_list = [0] * len(data)

    for i in data:
        ind = index.index(i)
        loc = count_num[ind]
        ordered_list[loc-1] = i
        count_num[ind] -= 1
    print(ordered_list)


data = [2,3,100,1,300,1,1]
print(counting_sort(data))