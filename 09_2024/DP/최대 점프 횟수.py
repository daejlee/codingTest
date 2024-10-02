import sys
INT_MIN = -sys.maxsize
n = int(sys.stdin.readline())
lst = [int(x) for x in sys.stdin.readline().split()]
# dp[i] == 해당 위치까지 왔을 때의 최대 점프 횟수
dp = [INT_MIN for _ in range(n)]
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if dp[j] == INT_MIN:
            continue
        if j + lst[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(max(dp))