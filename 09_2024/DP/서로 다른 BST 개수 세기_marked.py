n = int(input())
dp = [-1 for _ in range(20)]


def get_num_of_unique_bst(n):
    num = 0
    for i in range(n):
        num += dp[i] * dp[n - i - 1]
    return num


dp[0] = dp[1] = 1
dp[2] = 2
dp[3] = 5
for i in range(3, n + 1):
    dp[i] = get_num_of_unique_bst(i)
print(dp[n])
# 0913: 루트 노드를 어떤 값을 설정하느냐 -> 이 아이디어로 전개
# 0915: 왜 큰 문제를 작은 문제로 안 나누니... 하위 dp값을 이용해서 쌓아올리는 방식으로 전개한다는 아이디어에 익숙해지라.
# 0922: 복기
# 1014: 복기
