import sys

INT_MAX = sys.maxsize
# n: 원소 개수, m: 만들어야 하는 합
n, m = map(int, sys.stdin.readline().split())
lst = [int(x) for x in sys.stdin.readline().split()]
# dp[k] == k 만큼의 값을 만드는데 사용되는 최소 수열의 갯수
dp = [INT_MAX for _ in range(m + 1)]
dp[0] = 0
for i in range(n):
    for j in range(m, -1, -1):
        if j >= lst[i]:
            if dp[j - lst[i]] == INT_MAX:
                continue
            dp[j] = min(dp[j], dp[j - lst[i]] + 1)
if dp[-1] == INT_MAX:
    print("No")
else:
    print("Yes")
