import sys
import copy


# 1107: 모든 케이스를 해결하지 못했다. DP에 저장할 상태 정의를 잘못 정의했다.
def old():
    INT_MIN = -sys.maxsize
    n = int(sys.stdin.readline())
    lst = [0] + [int(x) for x in sys.stdin.readline().split()]
    m = sum(lst)
    # sum(A) == sum(B)이고 그 합이 최대가 되도록
    # dp[i][j]: i번째 숫자까지 체크했을 때 합으로 j를 만들 수 있으면 사용하지 않은 리스트(근데 이게 2개 이상이면?), 없으면 빈 리스트
    mid_idx = m // 2
    dp = [[[] for _ in range(mid_idx + 1)] for _ in range(n + 1)]
    dp[0][0] = copy.deepcopy(lst)

    # 주어진 미사용된 숫자들 dp_lst를 가지고 s를 만들 수 있다면 True 아니면 False
    def can_make_second(s, dp_lst):
        l = len(dp_lst)
        second_dp = [False for _ in range(s + 1)]
        second_dp[0] = True
        dp_lst.sort()
        for i in range(1, l):
            val = dp_lst[i]
            if val > s:
                break
            for j in range(s, -1, -1):
                if j >= val and second_dp[j - val]:
                    second_dp[j] = True
        return second_dp[s]

    for i in range(1, n + 1):
        for j in range(mid_idx + 1):
            if j >= lst[i] and len(dp[i - 1][j - lst[i]]):  # 사용할 때
                dp[i][j] = copy.deepcopy(dp[i - 1][j - lst[i]])
                dp[i][j].remove(lst[i])
            if len(dp[i - 1][j]):  # 안 사용할 때
                dp[i][j] = copy.deepcopy(dp[i - 1][j])
    ans = 0
    for j in range(mid_idx + 1):
        if len(dp[n][j]) and can_make_second(j, dp[n][j]):
            ans = max(ans, j)

    print(ans)
