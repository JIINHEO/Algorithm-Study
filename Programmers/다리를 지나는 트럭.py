def solution(bridge_length, weight, truck_weights):
    truck_on_bridge = [0] * bridge_length
    time = 0

    while len(truck_on_bridge):
        time += 1
        truck_on_bridge.pop(0)

        if truck_weights:
            if sum(truck_on_bridge) + truck_weights[0] <= weight: # 다리가 트럭의 무게를 버틸 수 있다면
                truck_on_bridge.append(truck_weights[0])
                truck_weights.pop(0)
            else: #다리가 트럭의 무게를 버틸 수 없다면
                truck_on_bridge.append(0)

    return time


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(2, 10,  [7, 4, 5, 6]))
print(solution(100, 100 ,[10]))
print(solution(100, 100 ,[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
