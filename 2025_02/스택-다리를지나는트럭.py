# while True에서 시간 카운트를 하나씩 늘려가며 처리한다.
# 카운트 증가 당 트럭을 이동시킨다.
# 만약 올라가있는 트럭의 무게 + 올라갈 트럭의 무게 <= 다리 한계이고 다리가 꽉 차있지 않으면 현 트럭을 push한다.
# 트럭이 다리를 빠져나가면 pop 한다.
# 트럭을 모두 이동시키면 종료하고 값을 리턴한다.

from collections import deque


def solution(bridge_length, weight, truck_weights):
    t = 0
    q = deque()
    i = 0
    w_s = 0
    while i < len(truck_weights) or len(q) > 0:
        t += 1
        for item in q:
            item[1] += 1
        if len(q) > 0 and q[0][1] > bridge_length:
            w_s -= q[0][0]
            q.popleft()

        if (
            i < len(truck_weights)
            and w_s + truck_weights[i] <= weight
            and len(q) < bridge_length
        ):
            q.append([truck_weights[i], 1])
            w_s += truck_weights[i]
            i += 1

    return t
