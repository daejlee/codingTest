import sys


# 11/18: 특정 케이스에 대해 동작하지 않음. 모두 커버하지 못하거나, 오버하여 구하는 경우가 있는듯
def old():
    INT_MIN = -sys.maxsize
    n = int(sys.stdin.readline())
    coins = [0]
    coins += [int(x) for x in sys.stdin.readline().split()]
    chance = 3
    # dp[i][j] -> i번 홀수 점프를 하였을 때 j번째 계단까지 올라왔을 때의 동전의 최대 합
    dp = [[INT_MIN for _ in range(n + 1)] for _ in range(chance + 1)]
    for i in range(chance + 1):
        dp[i][0] = 0

    for i in range(chance + 1):
        for j in range(1, n + 1):
            # 홀수 점프 했을 때
            if i and dp[i - 1][j - 1] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coins[j])
            # 홀수 점프 안 했을 때
            if j >= 2 and dp[i][j - 2] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i][j - 2] + coins[j])

    ans = max(dp[3])
    for elem in dp:
        for i in range(len(elem)):
            if elem[i] == INT_MIN:
                elem[i] = 0
        # print(elem)
    print(ans)


n = int(sys.stdin.readline())
coins = [0]
coins += [int(x) for x in sys.stdin.readline().split()]
chance = 3
# dp[i][j] -> i번째 계단까지 올라왔을 때 j번 홀수 점프를 하였을 때 동전의 최대 합
dp = [[0 for _ in range(chance + 1)] for _ in range(n + 1)]
dp[1][1] = coins[1]
if n > 1:
    dp[2][0] = coins[2]
    dp[2][2] = coins[1] + coins[2]

for i in range(3, n + 1):
    for j in range(chance + 1):
        # 홀수 점프 안 했을 때
        if dp[i - 2][j]:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coins[i])
        # 홀수 점프 했을 때
        if j and dp[i - 1][j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coins[i])

ans = max(
    dp[n]
)  # 왜 n번째만 체크? -> n번째 계단까지 올라왔을 때의 최대값을 구하는 것이므로. 다 순회하면 오버해서 구한다
print(ans)

# 11/26: 복기