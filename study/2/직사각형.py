from sys import stdin


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    h1 = y2 - y1
    w1 = x2 - x1
    h2 = y4 - y3
    w2 = x4 - x3
    # 좌하단 우하단 우상단 좌상단
    dxs, dys = [x3, x4, x4, x3], [y3, y3, y4, y4]
    dxs2, dys2 = [x1, x2, x2, x1], [y1, y1, y2, y2]
    for x, y in zip(dxs, dys):
        if x1 < x < x2 and y1 < y < y2:
            print("a")
            return
    for x, y in zip(dxs2, dys2):
        if x3 < x < x4 and y3 < y < y4:
            print("a")
            return
    if (x3 <= x1 <= x2 <= x4 and y1 <= y3 <= y4 <= y2) or (
        x1 <= x3 <= x4 <= x2 and y3 <= y1 <= y2 <= y4
    ):
        print("a")
        return

    for x, y in zip(dxs, dys):
        dot = 0
        if (
            (x1 == x and y1 == y)
            or (x1 == x and y2 == y)
            or (x2 == x and y1 == y)
            or (x2 == x and y2 == y)
        ):
            dot += 1
    if dot == 1:
        print("c")
        return
    for x, y in zip(dxs2, dys2):
        dot = 0
        if (
            (x3 == x and y3 == y)
            or (x3 == x and y4 == y)
            or (x4 == x and y3 == y)
            or (x4 == x and y4 == y)
        ):
            dot += 1
    if dot == 1:
        print("c")
        return
    intersect = 0
    for x, y in zip(dxs, dys):
        # print(x1, x, x2, y1, y, y2, x1 <= x <= x2, y1 <= y <= y2)
        if x1 <= x <= x2 and y1 <= y <= y2:
            intersect += 1
    if intersect == 0:
        print("d")
        return
    intersect = 0
    for x, y in zip(dxs2, dys2):
        # print(x1, x, x2, y1, y, y2, x1 <= x <= x2, y1 <= y <= y2)
        if x3 <= x <= x4 and y3 <= y <= y4:
            intersect += 1
    if intersect == 0:
        print("d")
        return
    else:
        print("b")
    # for x, y in zip(dxs2, dys2):
    #     intersect = 0
    #     print(x3, x, x3, y3, y, y4)
    #     if x3 <= x <= x4 and y3 <= y <= y4:
    #         intersect += 1
    # if intersect == 0:
    #     print("d")
    #     return
    # else:
    #     print("b")


for _ in range(4):
    # x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, stdin.readline().split())
    check(x1, y1, x2, y2, x3, y3, x4, y4)
