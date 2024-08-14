import sys

sys.setrecursionlimit(10**5)  # 재귀 깊이 설정
n, m = map(int, input().split())
highest = 0
mat = []
ans = [1, 0]
visited = []
for _ in range(n):
    buf = [int(x) for x in input().split()]
    highest = max(highest, max(buf))
    mat.append(buf)


def search(row, col, k):
    global visited

    if (
        row < 0
        or col < 0
        or row > n - 1
        or col > m - 1
        or visited[row][col] == True
        or mat[row][col] <= k
    ):
        return
    visited[row][col] = True
    search(row - 1, col, k)
    search(row + 1, col, k)
    search(row, col + 1, k)
    search(row, col - 1, k)


# K를 늘려가며 안전지대를 탐색한다.
def DFS():
    global highest, ans, visited

    for k in range(1, highest):
        visited = [[False for _ in range(m)] for _ in range(n)]
        comfort_zone = 0
        for row in range(n):
            for col in range(m):
                # 이미 방문했거나 물에 잠긴 좌표는 넘어간다.
                if visited[row][col] == True or mat[row][col] <= k:
                    continue
                comfort_zone += 1
                search(row, col, k)
        if comfort_zone > ans[1]:
            ans = [k, comfort_zone]


DFS()
for item in ans:
    print(item, end=" ")
