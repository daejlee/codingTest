n = int(input())
mat = []
visited = [[False for _ in range(n)] for _ in range(n)]
ans = [0, 0] # 터지는 블럭 수, 최대 블럭 크기
curr_block = 0
for _ in range(n):
    mat.append([int(x) for x in input().split()])

def search(row, col, target):
    global curr_block

    if row < 0 or col < 0 or row > n - 1 or col > n - 1:
        return
    if visited[row][col] == True:
        return
    if mat[row][col] != target:
        return
    visited[row][col] = True
    curr_block += 1
    if curr_block == 4:
        ans[0] += 1
    search(row - 1, col, target)
    search(row + 1, col, target)
    search(row, col - 1, target)
    search(row, col + 1, target)

def DFS():
    global curr_block

    for row in range(n):
        for col in range(n):
            if visited[row][col] == True:
                continue
            curr_block = 0
            search(row, col, mat[row][col])
            ans[1] = max(ans[1], curr_block)

DFS()
for item in ans:
    print(item, end=' ')