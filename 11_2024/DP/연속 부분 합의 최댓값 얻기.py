import sys
INT_MIN = -sys.maxsize
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
# DP STATE: 지금의 idx i와 지금까지의 연속 부분수열의 합 m가 같으면 같은 경우다.
# dp[i]: arr[i]까지 고려하였을 때 선택 부분 수열의 합의 최대
dp = [INT_MIN for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))