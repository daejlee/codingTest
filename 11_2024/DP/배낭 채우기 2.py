import sys

INT_MIN = -sys.maxsize
n, m = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(n):
    jewels.append([int(x) for x in sys.stdin.readline().split()])
jewels.sort()

# 무게 k를 만드는 최대의 가치
dp = [INT_MIN for _ in range(m + 1)]
dp[0] = 0

for i in range(n):
    curr_w, curr_v = jewels[i]
    for j in range(m + 1):
        if j >= curr_w:
            if dp[j - curr_w] == INT_MIN:
                continue
            dp[j] = max(dp[j], dp[j - curr_w] + curr_v)
print(max(dp))
