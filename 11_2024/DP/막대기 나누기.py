import sys

INT_MIN = -sys.maxsize
n = int(sys.stdin.readline())
# k 길이의 막대기를 팔았을 때 수익
revenue = [0]
revenue += [int(x) for x in sys.stdin.readline().split()]
# k 길이의 막대기를 나눴을 때의 최대 수익
dp = [INT_MIN for _ in range(n + 1)]
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = revenue[i]
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + dp[i - j])
print(max(dp))
