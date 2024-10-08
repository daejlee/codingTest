# import sys

# n = int(sys.stdin.readline())
# lst = [int(x) for x in sys.stdin.readline().split()]
# # i번째 원소로 시작했을 때의 최장 증가-감소 부분 수열
# ans = 0
# dp = [[] for _ in range(n)]


# # 단조 증가 / 단조 감소 / 증가하다가 감소하는 경우
# def is_valid(j, appendix):
#     buf = dp[j][:]
#     buf.append(appendix)
#     is_ascending = True
#     for i in range(1, len(buf)):
#         if buf[i] < buf[i - 1]:
#             is_ascending = False
#         elif buf[i] > buf[i - 1] and is_ascending == False:
#             return False
#     return True


# for i in range(n):
#     dp[i].append(lst[i])
#     for j in range(i):
#         if is_valid(j, lst[i]):
#             dp[j].append(lst[i])
# for item in dp:
#     if len(item) > ans:
#         ans = len(item)

# print(dp)
# print(ans)
# 1008: 해결 실패.. 유일하게 찾은 해결법은 시간 초과가 났다.

import sys

n = int(sys.stdin.readline())
lst = [int(x) for x in sys.stdin.readline().split()]
# i번째 원소로 끝났을 때, 현재 증-감 상태가 j일 때 부분 수열 중 최장 증가-감소 부분 수열의 길이
ans = 0
dp = [[0] * 2 for _ in range(n)]

for i in range(n):
    dp[i][0] = 1
    dp[i][1] = 1

    for j in range(i):
        if (
            lst[j] < lst[i]
        ):  # 계속 증가하는 경우, i보다 앞에 있는 것 중 lst[i]보다 작은 곳에 붙였을 떄의 최장 길이 계산
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif (
            lst[j] > lst[i]
        ):  # 계속 감소하는 경우, i보다 앞에 있는 것 중 lst[i]보다 큰 곳에 붙였을 떄의 최장 길이 계산
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
    dp[i][1] = max(
        dp[i][1], dp[i][0]
    )  # 현재 위치에서 증가를 멈추고 감소하는 경우, 이때 j=0 값이 j=1로 옮겨질 수 있음.

for i in range(n):
    for j in range(2):
        ans = max(ans, dp[i][j])

print(ans)
# 1007: 증가, 감소 상태 둘의 최장 증가 수열 길이를 DP에 저장해놓는다.
# 1008: 복기
