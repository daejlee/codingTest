from collections import deque
import math
n, k = map(int, input().split())
mat = []
removed_mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
    removed_mat.append(mat[-1])
is_visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()
walls = []
selected_walls = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            walls.append((i, j))
ans = math.inf
start_x, start_y = map(int, input().split())
start_x -= 1
start_y -= 1
dest_x, dest_y = map(int, input().split())
dest_x -= 1
dest_y -= 1
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]

def init_is_visited():
    for i in range(n):
        for j in range(n):
            is_visited[i][j] = False

def is_possible(x, y):
    # if 0 <= x < n and 0 <= y < n:
    #     print((mat[x][y] == 0 or (x, y) in selected_walls))
    if 0 <= x < n and 0 <= y < n and is_visited[x][y] == False and (mat[x][y] == 0 or (x, y) in selected_walls):
        return True
    return False

def BFS():
    global ans
    q.append((start_x, start_y, 0))

    while q:
        x, y, step = q.popleft()
        if is_visited[x][y] == True:
            continue
        if x == dest_x and y == dest_y:
            ans = min(ans, step)
            continue
        is_visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_possible(nx, ny):
                q.append((nx, ny, step + 1))

# k개의 벽을 없애는 경우의 수 조합을 전개하며 BFS한다.
def get_comb(idx):
    if len(selected_walls) >= k:
        init_is_visited()
        BFS()
        return
    for i in range(idx, len(walls)):
        selected_walls.append(walls[i])
        get_comb(idx + 1)
        selected_walls.pop()

get_comb(0)

if ans == math.inf:
    print(-1)
else:
    print(ans)