# Prev code: 사다리타기 구현을 너무 복잡하게 생각했음.
# def run_ladder(lines):
#     res = [0 for x in range(n)]
#     for i in range(1, n + 1):
#         x, y = i, 0
#         while y <= max_h:
#             # Find starting point
#             start = 0
#             while abs(x - lines[start][0]) > 1 or lines[start][1] < y:
#                 start += 1
#             y = lines[start][1] + 1
#             if x <= lines[start][0]:  # Go right
#                 x += 1
#             else:
#                 x -= 1
#         print(x)
#         res[x] = i
#     return res

n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a - 1))
lines.sort()
selected_lines = []
ans = m


def run_ladder():
    num1, num2 = [i for i in range(n)], [i for i in range(n)]

    # 사다리 타는 부분 유심히 볼 것
    for _, idx in lines:
        num1[idx], num1[idx + 1] = num1[idx + 1], num1[idx]
    for _, idx in selected_lines:
        num2[idx], num2[idx + 1] = num2[idx + 1], num2[idx]

    for i in range(n):
        if num1[i] != num2[i]:
            return False
    return True


def find_min_lines(cnt):
    global ans

    if cnt == m:
        if run_ladder():
            ans = min(ans, len(selected_lines))
        return

    # 조합 전개하는 부분 유심히 볼 것
    selected_lines.append(lines[cnt])
    find_min_lines(cnt + 1)
    selected_lines.pop()

    find_min_lines(cnt + 1)


find_min_lines(0)
print(ans)

# 0723
# 0724
