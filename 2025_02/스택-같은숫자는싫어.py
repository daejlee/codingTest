# 스택에 arr의 숫자들을 순서대로 푸시한다.
# 푸시할 때, top의 원소가 푸시할 원소와 같으면 넘어간다
# 끝나면 스택의 원소들을 출력한다

from collections import deque


def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    q = deque()
    for num in arr:
        if len(q) and q[-1] == num:
            continue
        q.append(num)
    return list(q)
