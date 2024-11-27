import sys

n, m = map(int, sys.stdin.readline().split())
jewel = []
for _ in range(n):
    jewel.append([int(x) for x in sys.stdin.readline().split()])
jewel.sort()
INT_MIN = -sys.maxsize
# 정확히 무게 k을 채울 수 있는 보석의 가치
# dp[k] = 1~k dp 중 현재 i번째 보석의 무게와 맞아 떨어지는 값과 더한 값
dp = [INT_MIN for _ in range(m + 1)]
dp[0] = 0
for i in range(n):
    curr_w, curr_val = jewel[i]
    for j in range(m, -1, -1):
        if j >= curr_w:
            if dp[j - curr_w] == INT_MIN:
                continue
            dp[j] = max(dp[j], dp[j - curr_w] + curr_val)
print(max(dp))

# 11/28: 마지막 복기. 백지에서 막힘없이 풀어내었음. 끝!
# 핵심은 인덱스를 거꾸로 돌려서 중복을 제거하는 것이다.