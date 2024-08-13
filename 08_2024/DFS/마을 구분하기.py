n = int(input())
mat = []
visited = []
towns = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
    visited.append([False for _ in range(n)])


def proceed(row, col):
    if (
        row < 0
        or col < 0
        or row > n - 1
        or col > n - 1
        or mat[row][col] == 0
        or visited[row][col] == True
    ):
        return
    visited[row][col] = True
    towns[-1] = towns[-1] + 1
    proceed(row + 1, col)
    proceed(row - 1, col)
    proceed(row, col + 1)
    proceed(row, col - 1)


def DFS():
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True or mat[i][j] == 0:
                continue
            towns.append(0)
            proceed(i, j)


DFS()
towns.sort()
print(len(towns))
for item in towns:
    print(item)
