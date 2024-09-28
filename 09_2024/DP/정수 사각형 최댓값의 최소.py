import sys

n = int(sys.stdin.readline())
mat = []
dp = [[-1 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    mat.append([int(x) for x in sys.stdin.readline().split()])


def init_fill():
    dp[0][0] = mat[0][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], mat[i][0])
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], mat[0][i])


init_fill()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), mat[i][j])
print(dp[-1][-1])
