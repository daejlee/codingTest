AVAILABLE = 0
WALL = 1
PERSON = 2
SHELTER = 3
# 사람 위로 지나갈 수 있음. 벽만 뚫지 못하는 것임
from collections import deque
n, h, m = map(int, input().split())
mat = []
is_visited = [[False for _ in range(n)] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
start_points = []
q = deque()
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
for i in range(n):
    mat.append([int(x) for x in input().split()])

def init_is_visited():
    for i in range(n):
        for j in range(n):
            is_visited[i][j] = False

for i in range(n):
    for j in range(n):
        if mat[i][j] != SHELTER:
            continue
        q.append((i, j, 0))
        init_is_visited()
        while q:
            x, y, step = q.popleft()
            if is_visited[x][y] == True:
                continue
            is_visited[x][y] = True
            if mat[x][y] == PERSON:
                if ans[x][y] != 0: # 이미 셸터로의 경로가 존재
                    local_step = min(step, ans[x][y])
                else:
                    local_step = step
                ans[x][y] = local_step
                found = True
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and is_visited[nx][ny] == False and mat[nx][ny] != 1:
                    q.append((nx, ny, step + 1))

for i in range(n):
    for j in range(n):
        if mat[i][j] == 2 and ans[i][j] == 0:
            ans[i][j] = -1

for item in ans:
    for elem in item:
        print(elem, end=" ")
    print()