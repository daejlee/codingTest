n = int(input())
mat = []
is_checked = []
ans = 0
for _ in range(n):
    mat.append([int(x) for x in input().split()])


# 체크된 원소에 대해 최대값을 구해 반환한다.
def get_max():
    res = 10000
    for item in is_checked:
        res = min(res, mat[item[0]][item[1]])
    return res


def is_occupied(row, col):
    for item in is_checked:
        if row == item[0] or col == item[1]:
            return True
    return False


# 현재 레벨을 순회하며 가능한 조합을 모두 찾는다.
def get_max_in_min(curr_level):
    global ans
    if curr_level >= n:
        ans = max(ans, get_max())
        return

    for i in range(n):
        if is_occupied(curr_level, i) == True:
            continue
        is_checked.append([curr_level, i])
        get_max_in_min(curr_level + 1)
        is_checked.pop()


get_max_in_min(0)
print(ans)
