from collections import deque

q = deque()
n = int(input())
for _ in range(n):
    buf = input()
    for i in range(len(buf)):
        if len(q) > 0:
            last_p = q[len(q) - 1]
        else:
            last_p = None
        if last_p == None:
            last_p = buf[i]
            q.append(buf[i])
            continue
        if buf[i] != last_p and last_p == "(" and buf[i] == ")":
            q.pop()
            last_p = None
        else:
            q.append(buf[i])
            last_p = buf[i]

    if len(q) > 0:
        print("NO")
        q.clear()
    else:
        print("YES")
