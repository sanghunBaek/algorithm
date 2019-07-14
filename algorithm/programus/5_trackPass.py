



# 길이만큼 리스트를 만든다면??
# pop으로 뒤를 하나빼고 앞에다가 하나를 추가한다면?

def moveBridge(bridge, a):
    bridge.pop()
    bridge.insert(0, a)
    return bridge


def solution(bridge_length, weight, truck_weights):
    time = 0
    # answer = 0
    bridge = [0] * bridge_length
    total_weight = 0

    while(truck_weights):
        if(sum(bridge) + truck_weights[0] <= weight):
            a = truck_weights.pop(0)
            bridge = moveBridge(bridge, a)
            time += 1
            print("bridge : ",bridge)
            print("truck_weight : ", truck_weights)
            print("time1 : ",time)
        else:
            bridge.pop()
            bridge.insert(0, 0)
            time += 1
            print("bridge : ", bridge)
            print("truck_weight : ", truck_weights)
            print("time2 : ", time)

    return time

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# 이걸로 해본 결과 truck_weights가 0이된다고 while이 끝나면 안된다


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# 이걸로도 결국은 틀린거였음 최종적으로 8일때 다 건너야지 다 안건넌 상태


print(solution(bridge_length,weight,truck_weights))