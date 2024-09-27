import math
import sys

ans = math.inf
# n, k = map(int, sys.stdin.readline().split())
n, k = 20, 1
home = []
selected = []
for i in range(1, n + 1):
    # x, y = map(int, sys.stdin.readline().split())
    x, y = i, 0
    home.append((x, y))


def get_dist():
    global ans
    # 가장 가까운 대피소와 가장 멀리 떨어져 있는 집의 최솟값
    remaining_home = []
    for elem in home:
        if elem not in selected:
            remaining_home.append(elem)
        # print(selected, remaining_home)
    local_min_dist = -math.inf
    for h in remaining_home:
        closest_shelter = math.inf
        for s in selected:
            dist = abs(h[0] - s[0]) + abs(h[1] - s[1])
            if dist < closest_shelter:
                closest_shelter = dist
        if closest_shelter > local_min_dist:
            local_min_dist = closest_shelter
    ans = min(ans, local_min_dist)


def get_comb(idx):
    global n, k

    if len(selected) >= k:
        get_dist()
        return

    for i in range(idx, len(home)):
        selected.append(home[i])
        get_comb(i + 1)
        selected.pop()


get_comb(0)
print(ans)
