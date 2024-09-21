# from collections import deque

# q = deque()
# n = int(input())
# mat = []
# dp = [[-1 for _ in range(n)] for _ in range(n)]
# dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
# for _ in range(n):
#     mat.append([int(x) for x in input().split()])
# cells = []

# for i in range(n):
#     for j in range(n):
#         cells.append((mat[i][j], i, j))

# cells.sort()

# # mat의 모든 점을 순회하며 탐색한다.
# # 밟고 지나갈 수 있는 최대 칸의 수를 BFS로 탐색한다.
# # DP 배열에 각 지점에서의 최장 증가 수열의 값이 들어있다.


# def is_vaild(nx, ny, curr_val):
#     if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] > curr_val:
#         return True
#     return False


# def search(x, y):
#     q.append((x, y, 1))
#     while q:
#         sx, sy, step = q.popleft()
#         # if len(q) == 0:
#         #     last_step = step
#         dp[x][y] = max(dp[x][y], step)
#         for dx, dy in zip(dxs, dys):
#             nx, ny = sx + dx, sy + dy
#             if is_vaild(nx, ny, mat[sx][sy]):
#                 if dp[nx][ny] != -1:
#                     dp[x][y] = max(dp[x][y], step + dp[nx][ny])
#                 else:
#                     q.append((nx, ny, step + 1))


# while cells:
#     val, i, j = cells.pop(0)
#     if dp[i][j] == -1:
#         search(i, j)

# res = 0
# for i in range(n):
#     for j in range(n):
#         if dp[i][j] > res:
#             res = dp[i][j]
# print(res)

# 0920: 일반적인 BFS 문제로 접근하였으나 그래프 탐색이 필요없는 문제였다. DP를 "어떤 순서로 채워나가야 하는지"를 고민해야 했다.
# 0921: 복기
n = int(input())
mat = []
dp = [[1 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
for _ in range(n):
    mat.append([int(x) for x in input().split()])
cells = []
for i in range(n):
    for j in range(n):
        cells.append((mat[i][j], i, j))
cells.sort()


# 배열의 값 중 가장 작은 좌표를 시작으로 채워나간다. 이 경우 그래프 탐색이 필요 없으며, 상하좌우만 살피면 된다.
def is_valid(nx, ny, val):
    if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] > val:
        return True
    return False


for val, x, y in cells:
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, val):
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

res = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] > res:
            res = dp[i][j]
print(res)
