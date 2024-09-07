from collections import deque

EMPTY = 0
GOOD = 1
BAD = 2
time = 0
q = deque()
n, k = map(int, input().split())
is_visited = [[False for _ in range(n)] for _ in range(n)]
mat = []
ans = []
selected = []
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
for i in range(n):
    buf = [int(x) for x in input().split()]
    mat.append(buf)
    ans_buf = []
    for j in range(len(buf)):
        if buf[j] == EMPTY:
            ans_buf.append(-1)
            continue
        elif buf[j] == BAD:
            selected.append((i, j))
            ans_buf.append(0)
        else:
            ans_buf.append(-3)
    ans.append(ans_buf)


def init_is_visited():
    for i in range(n):
        for j in range(n):
            is_visited[i][j] = False


def possible(x, y):
    if 0 <= x < n and 0 <= y < n and is_visited[x][y] == False:
        return True
    return False


def BFS():
    global time

    init_is_visited()
    time += 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if possible(nx, ny) == False:
                continue
            is_visited[nx][ny] = True
            if mat[nx][ny] == GOOD:
                # print(selected)
                selected.append((nx, ny))
                # print(selected)
                mat[nx][ny] = BAD
                ans[nx][ny] = time


def proceed():
    while True:
        if len(selected) == 0:
            return
        while len(selected) != 0:
            q.append(selected.pop())
        BFS()


proceed()
for i in range(n):
    for j in range(n):
        if ans[i][j] == -3:
            ans[i][j] = -2

for row in ans:
    for elem in row:
        print(elem, end=" ")
    print()
