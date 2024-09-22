# n = int(input())
# mat = []
# # i, j까지 왔을 때의 지금까지의 최솟값
# dp = [[0 for _ in range(n)] for _ in range(n)]
# for _ in range(n):
#     mat.append([int(x) for x in input().split()])
# def init_fill():
#     dp[0][0] = mat[0][0]
#     for i in range(1, n):
#         dp[i][0] = min(dp[i - 1][0], mat[i][0])
#         dp[0][i] = min(dp[0][i - 1], mat[0][i])
# def search(x, y):
#     if x > n - 1 or y > n - 1:
#         return
#     if y < n - 1:
#         if dp[x][y + 1] >= min(dp[x][y], mat[x][y + 1]) and x != 0:
#             return
#         dp[x][y + 1] = min(dp[x][y], mat[x][y + 1])
#     if x < n - 1:
#         if dp[x + 1][y] >= min(dp[x + 1][y], mat[x][y]) and y != 0:
#             return
#         dp[x + 1][y] = min(dp[x][y], mat[x + 1][y])
#     search(x + 1, y)
#     search(x, y + 1)
# init_fill()
# search(0, 0)
# for row in dp:
#     print(row)
# print(dp[-1][-1])

n = int(input())
mat = []
# i, j까지 왔을 때의 지금까지의 최솟값
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    mat.append([int(x) for x in input().split()])


def init_fill():
    dp[0][0] = mat[0][0]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], mat[i][0])
        dp[0][i] = min(dp[0][i - 1], mat[0][i])


init_fill()
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(mat[i][j], max(dp[i - 1][j], dp[i][j - 1]))

print(dp[-1][-1])

# 0914: 시간 초과 발생. 점화식이 불완전했음.
# 0915: 복기 완료
# 0922: 복기
