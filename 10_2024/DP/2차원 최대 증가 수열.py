import sys

INT_MIN = -sys.maxsize
n, m = map(int, sys.stdin.readline().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in sys.stdin.readline().split()])
# i, j 좌표로 올 때 밟을 수 있는 최대 칸의 수
dp = [[INT_MIN for _ in range(m)] for _ in range(n)]

dp[0][0] = 1


# i, j까지 오는 최대 칸의 수를 구한다.
# [0 ~ i][0 ~ j]의 범위를 탐색한다.
def get_max_path(i, j):
    for x in range(i):
        for y in range(j):
            if dp[x][y] == INT_MIN:
                continue
            if mat[x][y] < mat[i][j]:
                dp[i][j] = max(dp[i][j], dp[x][y] + 1)


for i in range(n):
    for j in range(m):
        get_max_path(i, j)

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

# print(dp)

print(ans)
