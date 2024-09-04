import math
from collections import deque

n = int(input())
q = deque()
q.append((n, 0))
is_visited = [0 for _ in range(2 * n)]
ans = math.inf

# 현재 숫자와 스텝을 큐에 푸쉬한다.
# 2, 3으로 나눌 수 없으면 1을 더한다.
# 2, 3으로 동시에 나눌 수 있으면 각 경우의 수를 탐색한다.
# 2, 3 중 하나로만 나눌 수 있다면 나누는 경우의 수와 1을 더하는 경우의 수를 탐색한다.
# 각 경우의 수에 1을 빼는 조합을 전개한다.


def check_and_append(idx, step):
    idx = int(idx)
    if idx == 0:
        return
    if is_visited[idx] == 0 or is_visited[idx] > step:
        is_visited[idx] = step
        q.append((idx, step))


while q:
    num, step = q.popleft()
    if num == 0:
        continue
    elif num == 1:
        ans = min(ans, step)
        continue
    check_and_append(num - 1, step + 1)
    if num % 6 == 0:
        check_and_append(num / 2, step + 1)
        check_and_append(num / 3, step + 1)
    elif num % 2 == 0:
        check_and_append(num / 2, step + 1)
        check_and_append(num + 1, step + 1)
    elif num % 3 == 0:
        check_and_append(num / 3, step + 1)
        check_and_append(num + 1, step + 1)
    else:
        check_and_append(num + 1, step + 1)

print(ans)
