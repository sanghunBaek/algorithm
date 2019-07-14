# 중요한것 배열의 인덱스 슬라이싱에서 0:10 은 0<= 이고 <10 인거다
# 그리고 :a 라고했을때 a가 기존에 정해진 슬라이싱보다 많은경우에 오류가 안나고 기존의 것까지만 출력된다

a = input()

count = len(a)//10

count = count + 2
for i in range(1,count):
    c = 10*i
    d = 10*(i-1)
    print(a[d:c])