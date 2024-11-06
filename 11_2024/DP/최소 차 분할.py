import sys

INT_MAX = sys.maxsize
n = int(sys.stdin.readline())
arr = [0] + [int(x) for x in sys.stdin.readline().split()]
m = sum(arr)
# dp[i][j] - 지금까지 i번째 수까지만 고려했을 때
# 고른 수의 합을 j로 만드는 것이 가능하면 True, 불가능하면 False
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

dp[0][0] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        # arr[i]를 사용하여 j를 만든 경우 -> i - 1번째까지 고려하여 만든 수들의 합이 j - arr[i]여야 한다.
        # j < arr[i]인 경우 arr[i]를 추가하여 j가 될 수 없으므로 j >= arr[i]인 경우만 가능하다.
        if j >= arr[i] and dp[i - 1][j - arr[i]]:
            dp[i][j] = True
        # arr[i]를 선택하지 않고 합이 j가 된 경우 -> arr[i] 없이 합이 j가 되어야 한다.
        # i - 1번째까지 고려하여 고른 수의 합이 j여야 한다.
        if dp[i - 1][j]:
            dp[i][j] = True

ans = INT_MAX
for i in range(1, m):
    if dp[n][i]:
        ans = min(ans, abs(i - (m - i)))

print(ans)

# 1105: 구현 실패. 2차원 DP를 사용하는 법을 익히자.
