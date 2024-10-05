# n = int(input())
# mat = []
# for _ in range(n):
#     mat.append([int(x) for x in input().split()])
# res = 200
# # 최대 - 최소가 최소가 되도록.
# # 다른 말로 하면 최댓값과 최솟값 사이의 간격을 최소화하도록 이동하는 경로.


# def print_dp(dp):
#     for row in dp:
#         print(row)
#         print("")


# def init_fill():
#     dp[0][0] = (mat[0][0], mat[0][0], 0)
#     for i in range(1, n):
#         cur_max_min = max(dp[0][i - 1][0], mat[0][i])
#         cur_min_max = min(dp[0][i - 1][1], mat[0][i])
#         dp[0][i] = (cur_max_min, cur_min_max, cur_max_min - cur_min_max)
#         cur_max_min = max(dp[i - 1][0][0], mat[i][0])
#         cur_min_max = min(dp[i - 1][0][1], mat[i][0])
#         dp[i][0] = (cur_max_min, cur_min_max, cur_max_min - cur_min_max)


# def get_curr_dp(x, y, dp):
#     curr_val = mat[x][y]
#     # 최소의 최대, 최대의 최소. 왼쪽이랑 위쪽 본다.
#     max_min_1, min_max_1, diff_1 = (
#         dp[x][y - 1][0],
#         dp[x][y - 1][1],
#         dp[x][y - 1][2],
#     )  # 왼쪽
#     max_min_2, min_max_2, diff_2 = (
#         dp[x - 1][y][0],
#         dp[x - 1][y][1],
#         dp[x - 1][y][2],
#     )  # 위쪽
#     # 해당 좌표에서의 새로운 값
#     n_diff_1 = max(curr_val, max_min_1) - min(curr_val, min_max_1)
#     n_diff_2 = max(curr_val, max_min_2) - min(curr_val, min_max_2)
#     # print(x, y, n_diff_1, n_diff_2)
#     if n_diff_1 == n_diff_2:
#         n_dp = [arr[:] for arr in dp]
#         n_dp[x][y] = (max(curr_val, max_min_1), min(curr_val, min_max_1), n_diff_1)
#         start_dp(x, y + 1, n_dp)
#     if n_diff_1 > n_diff_2:
#         dp[x][y] = (max(curr_val, max_min_2), min(curr_val, min_max_2), n_diff_2)
#     else:
#         dp[x][y] = (max(curr_val, max_min_1), min(curr_val, min_max_1), n_diff_1)


# def start_dp(x, y, dp):
#     print("new\n", dp)
#     global res
#     # 현 좌표까지의 최소의 최대, 최대의 최소 값이 들어있음
#     init_fill()
#     for i in range(x, n):
#         for j in range(y, n):
#             get_curr_dp(i, j, dp)
#     # print_dp(dp)
#     res = min(res, dp[-1][-1][2])


# dp = [[(-1, -1, -1) for _ in range(n)] for _ in range(n)]
# start_dp(1, 1, dp)

# # print_dp()
# print(res)
# 0927: 2차원 DP로 접근했으나 실패, 3차원으로 시도 중 구현에 실패했다. 처음부터 3차원으로 접근하며 시도했더라면 가능했을 수도 있을듯..
# 값의 범위가 1~100이므로, 각각 모두 탐색해볼만 하다. lower, upper 바운드를 설정하여 양쪽에서 범위를 좁혀나가는 형식이다. 유연한 사고!

import sys

INT_MAX = sys.maxsize
n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
dp = [[INT_MAX for _ in range(n)] for _ in range(n)]
ans = INT_MAX


def init_fill():
    dp[0][0] = mat[0][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], mat[i][0])
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], mat[0][i])


def solve(lower_bound):
    for i in range(n):
        for j in range(n):
            if mat[i][j] < lower_bound:
                mat[i][j] = INT_MAX  # 돌아가지 않을 좌표이다. 초장에 틀어 막는다는 느낌

    init_fill()
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), mat[i][j])

    return dp[-1][-1]


for lower_bound in range(1, 101):
    upper_bound = solve(lower_bound)

    if upper_bound == INT_MAX:
        continue
    ans = min(ans, upper_bound - lower_bound)

print(ans)

# 0928: 복기. 돌아오지 않을 좌표들 INT_MAX로 틀어막는 부분
# 1005: 복기 - 풀이과정 접근이 쉽지 않다..
