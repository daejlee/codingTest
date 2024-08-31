from collections import deque
n, k, u, d = map(int, input().split())
mat = []
is_visited = []
selected_city = []
q = deque()
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
for _ in range(n):
    mat.append([int(x) for x in input().split()])
    is_visited.append([False for _ in range(n)])
ans = 0

# k: 고를 도시의 수
# u 이상 d 이하의 도시만 선택
# 고른 k개의 도시로부터 갈 수 있는 서로 다른 도시의 수를 최대화
# 상하좌우 인접한 도시, 높이 차가 u 이상 d 이하
# 64C3 = 32 * 63 * 21 -> 1800 * 21 -> 약 3만 콜

# 선택된 도시들을 시작점으로 하여 BFS 전개, 최댓값 업데이트
def check_selected_cities():
    global ans
    local_max = 0
    for i in range(n):
        for j in range(n):
            is_visited[i][j] = False
    for item in selected_city:
        q.append(item)

    while q:
        x, y = q.popleft()
        if is_visited[x][y] == True: continue
        local_max += 1
        is_visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and is_visited[nx][ny] == False and u <= abs(mat[x][y] - mat[nx][ny]) <= d:
                # print(nx, ny, mat[nx][ny])
                q.append((nx, ny))
    ans = max(ans, local_max)

# k개의 도시를 선택하는 조합 전개
def check_combination(row, col):
    if len(selected_city) >= k:
        # print(selected_city)
        check_selected_cities()
        return

    for i in range(row, n):
        for j in range(col, n):
            selected_city.append((i, j))
            check_combination(i, j)
            selected_city.pop()

check_combination(0, 0)
print(ans)