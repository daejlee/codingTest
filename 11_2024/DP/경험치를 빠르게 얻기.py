import sys

INT_MIN = -sys.maxsize
n, m = map(int, sys.stdin.readline().split())
quests = [[]]
e_max = t_max = 0
for _ in range(n):
    e, t = map(int, sys.stdin.readline().split())
    e_max += e
    t_max += t
    quests.append([e, t])

# 걸린 시간이 j일 때의 최대 경험치
dp = [INT_MIN for _ in range(t_max + 1)]
dp[0] = 0

for i in range(1, n + 1):
    curr_e, curr_t = quests[i]
    for j in range(t_max + 1, -1, -1):
        if j >= curr_t:
            if dp[j - curr_t] == INT_MIN:
                continue
            dp[j] = max(dp[j], dp[j - curr_t] + curr_e)

ans = -INT_MIN
for i in range(1, len(dp)):
    if dp[i] == INT_MIN or dp[i] < m:
        continue
    ans = min(ans, i)
if ans == -INT_MIN:
    print(-1)
else:
    print(ans)
