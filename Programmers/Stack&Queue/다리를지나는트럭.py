def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length  # 다리 길이만큼 스택생성

    while q:
        answer += 1  # 시간 1초 증가
        q.pop(0)
        if truck_weights:   # 대기 트럭이 있다면
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return answer
