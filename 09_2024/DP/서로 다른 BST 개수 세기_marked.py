n = int(input())
dp = [-1 for _ in range(20)]
def get_num_of_unique_bst(n):
    num = 0
    for i in range(n):
        num += dp[i] * dp[n - i - 1]
    return num

dp[0] = dp[1] = 1
dp[2] = 2
dp[3] = 5
for i in range(3, n + 1):
    dp[i] = get_num_of_unique_bst(i)
print(dp[n])