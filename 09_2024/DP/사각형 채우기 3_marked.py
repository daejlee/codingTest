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
    dp[i] = 2 * dp[i - 1] + 3 * dp[i - 2] % div
    for j in range(i - 1, -1, -1):
        dp[i] += 2 * dp[j] % div
print(dp[n] % div)
# 0911: 해설 보고 풀었지만 아직 이해가 안 간다.. 계속 연습하자.
# 0915: i - 1, i - 2, i - 3~0까지의 범위를 모두 고려하라.
