import sys


def old():
    n = int(sys.stdin.readline())
    # 상대
    cards_a = [0] + [int(x) for x in sys.stdin.readline().split()]
    # 남우
    cards_b = [0] + [int(x) for x in sys.stdin.readline().split()]
    print(cards_a, cards_b)
    m = sum(cards_b)
    INT_MIN = -sys.maxsize
    # dp[i][j]: a가 i번째, b가 j번째까지 고려했을 때 얻은 최대 점수
    dp = [[INT_MIN for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 대결하는 경우
            if cards_a[i] > cards_b[j] and dp[i][j - 1] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + cards_b[j])
            elif cards_a[i] < cards_b[j] and dp[i - 1][j] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            # 대결하지 않거나 비긴 경우
            if dp[i - 1][j - 1] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
    for elem in dp:
        for i in range(len(elem)):
            if elem[i] == INT_MIN:
                elem[i] = 0
        print(elem)
    ans = max(dp[n])
    print(ans)
    # 11/19: 접근 실패.. 무엇을 DP State로 삼아야 할지 감이 안잡힌다.


n = int(sys.stdin.readline())
cards_a = [0] + [int(x) for x in sys.stdin.readline().split()]
cards_b = [0] + [int(x) for x in sys.stdin.readline().split()]

# dp[i][j]: a가 i번째, b가 j번째까지 버렸을 때 얻은 최대 점수
dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        # 대결할 때 - a가 더 작을 때
        if cards_a[i + 1] < cards_b[j + 1]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # 대결할 때 - b가 더 작을 때
        if cards_a[i + 1] > cards_b[j + 1]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + cards_b[j + 1])
        # 버리기
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
ans = 0
for i in range(n + 1):
    ans = max(ans, dp[i][n])
    ans = max(ans, dp[n][i])

print(ans)
# 11/19: 접근한 로직 자체는 비슷한데, 전진하는 부분이 불완전했다.
