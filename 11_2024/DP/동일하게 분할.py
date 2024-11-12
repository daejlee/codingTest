import sys
n = int(sys.stdin.readline())
arr = [0]
arr += [int(x) for x in sys.stdin.readline().split()]
m = sum(arr)
if m % 2: # 총 합이 홀수면 반으로 나눌 수 없음
    print('No')
    exit()

# dp[i][j] i번째 수까지 고려했을 때 j를 만들 수 있는지
dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    curr_v = arr[i]
    for j in range(m + 1):
        # arr[i]를 사용할 때: i - 1번째 수까지 사용했을 때 j - arr[i]가 존재해야 함
        if j >= curr_v and dp[i - 1][j - curr_v]:
            dp[i][j] = True
        # arr[i]를 사용하지 않을 때: i - 1번째 수까지 사용했을 때 j가 존재해야 함
        if dp[i - 1][j]:
            dp[i][j] = True

if dp[n][m // 2]:
    print('Yes')
else:
    print('No')