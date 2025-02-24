# 큐를 선언해 s의 문자를 순회하며 push 한다.
# 만일 큐에 짝지어진 괄호가 있으면 pop 한다.
# 순회가 끝났을 때 큐에 원소가 남아있으면 false, 비어 있으면 true

from collections import deque

def solution(s):
    q = deque()
    for c in s:
        if len(q) != 0:
            if q[0] == '(' and c == ')':
                q.popleft()
                continue
        q.append(c)
    if len(q) == 0:
        return True
    else:
        return False