n = int(input())
div = 1000000007
# tabulation, bottom-up approach
dp = [-1 for _ in range(n + 2)]
# print(dp)
dp[0] = 1
dp[1] = 2
if n > 1:
    dp[2] = 7
for i in range(3, n + 1):
    dp[i] = (3 * dp[i - 1]) + dp[i - 2] - dp[i - 3]
print(dp[n] % div)
# 0911: 해설 보고 풀었지만 아직 이해가 안 간다.. 계속 연습하자.
