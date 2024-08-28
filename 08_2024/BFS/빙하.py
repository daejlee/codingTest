from collections import deque

q = deque()
n, m = map(int, input().split())
mat = []
is_visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    mat.append([int(x) for x in input().split()])
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
ans = 0
last_melt = 0


# 가장 바깥쪽 부터 BFS 탐색하며 만나는 빙하를 녹인다.
# mat를 깊은 복사해서 버퍼로 사용한다. -> 이걸 다음 순회에 사용한다.
# 녹은 빙하의 크기도 같이 기록한다.
def BFS():
    global mat, q
    melt = 0
    next_mat = [arr[:] for arr in mat]
    next_q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if is_visited[x][y] == True:
            continue
        if (
            mat[x][y] == 1
        ):  # 이거. 녹인 좌표를 시작점 삼아 다음 BFS를 진행하면 시간복잡도가 획기적으로 줄어든다.
            if next_mat[x][y] == 1:
                melt += 1
                next_mat[x][y] = 0
                next_q.append((x, y))
            continue
        is_visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and is_visited[nx][ny] == False:
                q.append((nx, ny))
    mat = next_mat
    q = next_q
    return melt


while True:
    melt = BFS()
    if melt == 0:
        break
    ans += 1
    last_melt = melt

print(ans, last_melt)
