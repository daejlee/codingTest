# from collections import deque
# n, k, m = map(int, input().split())
# mat = []
# visited = [[False for _ in range(n)] for _ in range(n)]
# for _ in range(n):
#     mat.append([int(x) for x in input().split()])
# q = deque()
# for _ in range(k):
#     r, c = map(int, input().split())
#     q.append((r - 1, c - 1))
# 시작점들 중심으로 완전 탐색하되 돌을 만날 때 마다 재귀해서 경우의 수 탐색
# 위 코드 - 실패한 이유 백트레킹 아이디어는 얻었지만 돌을 만날 때 마다 재귀하는 방법 보다는 돌 중 2개를 선택하는 경우의 수를 구하는 것이 효율적이다.
# 결국 확신이 없었다

from collections import deque

ans = 0
n, k, m = map(int, input().split())
mat = []
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    mat.append([int(x) for x in input().split()])

s_pos = []
for _ in range(k):
    r, c = map(int, input().split())
    s_pos.append((r - 1, c - 1))

stone_pos = [(i, j) for i in range(n) for j in range(n) if mat[i][j] == 1]
selected_stones = []
q = deque()


def bfs():
    while q:
        x, y = q.popleft()
        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not mat[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True


def calc():
    for x, y in selected_stones:
        mat[x][y] = 0
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    for x, y in s_pos:
        q.append((x, y))
        visited[x][y] = True
    bfs()
    for x, y in selected_stones:
        mat[x][y] = 1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    return cnt


def find_max(idx, cnt):
    global ans
    if idx == len(stone_pos):
        if cnt == m:
            ans = max(ans, calc())
        return

    selected_stones.append(stone_pos[idx])
    find_max(idx + 1, cnt + 1)
    selected_stones.pop()
    find_max(idx + 1, cnt)


find_max(0, 0)
print(ans)
