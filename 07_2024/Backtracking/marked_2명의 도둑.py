# 0723 prevCode: 왜 못 풀었을까? - 완전 탐색이고 최대 가치를 찾는 부분을 백트래킹 한다는 아이디어는 얻었지만, 깔끔한 구현을 하지 못했다.
# 실수 없이 간결하게 푸는 방법을 익힌다.
# def select_max(row, col, r):
#     if r == c:
#         return 0
#     region_max = 0
#     for i in range(m - r + 1):
#         w = 0
#         pow_sum = 0
#         for k in range(r):
#             pow_sum += pow(mat[row][col + i + k], 2)
#             w += mat[row][col + i + k]
#         if w <= c:
#             region_max = max(region_max, pow_sum)
#     return max(region_max, select_max(row, col, r + 1))
# def search(row, col, is_second):
#     region_max = 0
#     for row in range(n):
#         for col in range(n - m):
#             if is_second == False:
#                 second_thief = search(row, col + m, True)
#             w = 0
#             pow_sum = 0
#             for i in range(m):
#                 pow_sum += pow(mat[row][col + i], 2)
#                 w += mat[row][col + i]
#             if w > c:
#                 region_max = max(select_max(row, col, 1), region_max)
#             else:
#                 region_max = max(pow_sum, region_max)
#             if is_second == False:
#                 res = second_thief + region_max
#     if is_second == True:
#         return region_max

n, m, c = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
a = []
max_val = 0


def intersect(a, b, c, d):
    return not (b < c or d < a)


def possible(sx1, sy1, sx2, sy2):
    if sy1 + m - 1 >= n or sy2 + m - 1 >= n:
        return False
    if sx1 != sx2:
        return True
    if intersect(sy1, sy1 + m - 1, sy2, sy2 + m - 1):
        return False
    return True


def find_max_sum(curr_idx, curr_weight, curr_val):
    global max_val
    if curr_idx == m:
        if curr_weight <= c:
            max_val = max(max_val, curr_val)
        return
    # curr_idx index에 있는 숫자 선택 X
    find_max_sum(curr_idx + 1, curr_weight, curr_val)
    # curr_idx index에 있는 숫자 선택 O
    find_max_sum(
        curr_idx + 1, curr_weight + a[curr_idx], curr_val + a[curr_idx] * a[curr_idx]
    )


def find_max(sx, sy):
    global a, max_val
    a = mat[sx][sy : sy + m]

    max_val = 0
    find_max_sum(0, 0, 0)
    return max_val


ans = max(
    [
        find_max(sx1, sy1) + find_max(sx2, sy2)
        for sx1 in range(n)
        for sy1 in range(n)
        for sx2 in range(n)
        for sy2 in range(n)
        if possible(sx1, sy1, sx2, sy2)
    ]
)

print(ans)
