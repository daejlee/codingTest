from collections import deque
q = deque()
n, k = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
row_start, col_start = map(int, input().split())
row_start, col_start = row_start - 1, col_start - 1
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
q.append((row_start, col_start))

# k 만큼 탐색 + 이동을 반복한다.
for i in range(k):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[row_start][col_start] = True
    curr_val = mat[row_start][col_start]
    dest_row, dest_col, dest_val = row_start, col_start, 0
    # print('INIT: ', row_start, col_start, curr_val)
    while q:
        row, col = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = col + dx, row + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] == True:
                    continue
                visited[ny][nx] = True
                if mat[ny][nx] < curr_val:
                    q.append((ny, nx))
                    if mat[ny][nx] > dest_val:
                        dest_val = mat[ny][nx]
                        dest_row, dest_col = ny, nx
                        # print(ny, nx, dest_val)
                    elif mat[ny][nx] == dest_val:
                        if ny < dest_row or (ny == dest_row and nx < dest_col):
                            dest_row, dest_col = ny, nx
                            # print(ny, nx, dest_val)
    if row_start == dest_row and col_start == dest_col:
        break
    row_start, col_start = dest_row, dest_col
    q.append((row_start, col_start))
print(dest_row + 1, dest_col + 1)