import sys

INT_MIN = -sys.maxsize
n = int(sys.stdin.readline())
lst = [[0, 0, 0]]
# 정렬되어 있을 때 k번째를 마지막으로 선택했을 때의 최대 값
dp = [INT_MIN for _ in range(n + 1)]
dp[0] = 0
for _ in range(n):
    lst.append([int(x) for x in sys.stdin.readline().split()])

for i in range(1, n + 1):
    for j in range(0, i):
        if lst[i][0] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + lst[i][2])

print(max(dp))
# 1024: 겹치지 않게 선분 고르기 2가 생각나서 봤더니, 완전 같은 로직같더라. 실제로 같은 로직이었는데 실수해서 처박음.
# 그런데 이 로직이 꽤 유용할 것 같아 복습하는 것이 좋겠다.
