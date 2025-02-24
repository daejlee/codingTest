# priorities를 순회하며 큐에 넣는다.
# 큐를 순서대로 pop 하면서 우선순위에서 밀리면 다시 push 한다.
# pop, push할 때는 location도 같이 업데이트 한다.
# pop할 때는 실행된 프로세스 개수를 늘린다.
# 타겟이 pop되면 지금까지 실행된 프로세스의 갯수 + 1을 리턴한다.
from collections import deque


def solution(priorities, location):
    exec_cnt = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])

    while True:
        curr = queue.popleft()
        if any(curr[1] < q[1] for q in queue):
            queue.append(curr)
        else:
            exec_cnt += 1
            if curr[0] == location:
                return exec_cnt


# any 쓰는 거 나쁘지 않네
