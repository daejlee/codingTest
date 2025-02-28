# 두 큐의 총합을 구해 2로 나누어 만들 값을 찾는다.
# pop하면 첫 번째가 추출되고, insert하면 끝에 추가됨
# 가능한 경우의 수는 2개다.
# 1에서 pop, 2에 insert
# 2에서 pop, 2에 insert
# 이거 순서가 안 바뀐다.
# 두 큐를 이어서 붙은 리스트에서 잘 나누어 합이 2등분되게 하면 된다.
import sys


# 자를 점을 찾는다.
def find_cut(queue1, queue2):
    concat_q = queue1 + queue2
    q_sum = sum(concat_q)
    ret = []
    for i in range(len(concat_q)):
        half_sum = 0
        for j in range(i, i + len(concat_q)):
            if j >= len(concat_q):
                j -= len(concat_q)
            half_sum += concat_q[j]
            if half_sum == q_sum // 2:
                ret.append([i, j])
            elif half_sum > q_sum:
                break
    if len(ret) > 0:
        return ret
    return -1


INT_MAX = sys.maxsize


def solution(queue1, queue2):
    cut_idx = find_cut(queue1, queue2)
    if cut_idx == -1:
        return -1
    ans = INT_MAX
    for region in cut_idx:
        curr_val = 0
        start = region[0]
        end = region[1]
        curr_val += start
        if end < len(queue1):
            curr_val += len(queue1) - end
        else:
            curr_val += end - len(queue1) + 1
        print(start, end)
        print(curr_val)
        ans = min(ans, curr_val)
    return ans


# 1시간, 타임아웃. 33.3/100


def solution(queue1, queue2):
    ans = 0

    target = (sum(queue1) + sum(queue2)) // 2
    n = len(queue1)
    start = 0
    end = n - 1
    cur = sum(queue1)
    queue3 = queue1 + queue2 + queue1
    while cur != target:
        if cur < target:
            end += 1
            if end >= len(queue3):
                return -1
            cur += queue3[end]
        elif cur > target:
            cur -= queue3[start]
            start += 1
        ans += 1
    return ans
