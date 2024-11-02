import sys

n = int(sys.stdin.readline())
lst = []
# dp[i] : x1 기준으로 정렬되어 있다는 가정 하에서
#         i번째 선분을 끝으로
#         겹치지 않게 선택할 수 있는 최대 선분의 수
dp = [0 for _ in range(n)]
for _ in range(n):
    lst.append([int(x) for x in sys.stdin.readline().split()])
# 오름차순 정렬 후, 각 선분에 대해 이전 선택 선분들과 겹치지 않으며 선택할 수 있는 선분 수를 dp
lst.sort()

for i in range(n):
    # 현재 선분이 시작 선분인 경우에는
    # dp값이 1이 되므로
    # 초기 셋팅은 1.
    dp[i] = 1

    for j in range(i):
        x1_i, _ = lst[i]
        _, x2_j = lst[j]

        if x2_j < x1_i:
            # i ~ j까지 가능한 것 중 제일 큰 갯수값을 사용한다.
            dp[i] = max(dp[i], dp[j] + 1)

ans = max(dp)
print(ans)

# 10/4: 정렬하기 전까진 순서가 없는 조합 문제라 dp 접근이 곤란했는데,
# 정렬하고 나니 순서가 생겨 접근이 가능했다.
# 10/5: 복기
# 10/12: 복기
# 11/2: 복기
