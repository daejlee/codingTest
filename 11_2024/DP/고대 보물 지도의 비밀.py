import sys

n, k = map(int, sys.stdin.readline().split())
path = [0] + [int(x) for x in sys.stdin.readline().split()]
# 일단 연속 부분합 최대 구해보자
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
dp[0][0] = 0

# dp[i][j] :: 음수가 i번 나타나고 path j번째 원소로 끝나는 부분합의 최대값
for i in range(k + 1):
    for j in range(n):
        # if dp[i][j] == -1: continue
        if path[j + 1] < 0:
            # 음수 사용
            if i < k:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + path[j + 1])
            # 음수 안 씀 - 이 수열은 여기서 끝이다
        else:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + path[j + 1])
ans = 0
for elem in dp:
    ans = max(ans, max(elem))
print(ans)
