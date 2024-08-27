# from collections import deque
# n, k, m = map(int, input().split())
# mat = []
# visited = [[False for _ in range(n)] for _ in range(n)]
# for _ in range(n):
#     mat.append([int(x) for x in input().split()])
# q = deque()
# for _ in range(k):
#     r, c = map(int, input().split())
#     q.append((r - 1, c - 1))
# 시작점들 중심으로 완전 탐색하되 돌을 만날 때 마다 재귀해서 경우의 수 탐색
# 위 코드 - 실패한 이유 백트레킹 아이디어는 얻었지만 돌을 만날 때 마다 재귀하는 방법 보다는 돌 중 2개를 선택하는 경우의 수를 구하는 것이 효율적이다.
# 결국 확신이 없었다
from collections import deque

n, k, m = map(int, input().split())
q = deque()
mat = []
is_visited = [[False for _ in range(n)] for _ in range(n)]
stones = []
selecetd_stones = []
start_cords = []
ans = 0
# x는 위아래, y는 양옆입니다.
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, -0]  # E N W S

for _ in range(n):
    mat.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            stones.append((i, j))

for _ in range(k):
    input_r, input_c = map(int, input().split())
    start_cords.append((input_r - 1, input_c - 1))
    q.append((input_r - 1, input_c - 1))

# 돌의 좌표 중에 m개를 선택하는 경우의 수를 백트레킹한다.
# 전개 과정은 BFS로 진행한다.


def push_start():
    for cord in start_cords:
        q.append((cord[0], cord[1]))


def init_visited():
    for i in range(n):
        for j in range(n):
            is_visited[i][j] = False


def remove_stones():
    for stone in selecetd_stones:
        mat[stone[0]][stone[1]] = 0


def restore_stones():
    for stone in selecetd_stones:
        mat[stone[0]][stone[1]] = 1


def get_local_sum():
    local_sum = 0

    while q:
        x, y = q.popleft()
        if is_visited[x][y] == True or mat[x][y] == 1:
            continue
        is_visited[x][y] = True
        local_sum += 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and is_visited[nx][ny] != True
                and mat[nx][ny] != 1
            ):
                # print("NX, NY: ", nx, ny)
                q.append((nx, ny))
        # print("QUEUE: ", q)
    # print('LOCAL_SUM: ', local_sum)
    return local_sum


# 돌 중 m개를 선택하는 조합의 경우의 수를 구해 백트레킹한다.
def backtrack(idx, cnt):
    global ans

    if idx == len(stones):
        if cnt == m:
            # print("SELECTED STONES: ", selecetd_stones)
            remove_stones()
            init_visited()
            ans = max(ans, get_local_sum())
            # print("REMOVED MAT: ", mat)
            # print("VISITED: ", is_visited)
            restore_stones()
            push_start()
        return

    selecetd_stones.append(stones[idx])
    backtrack(idx + 1, cnt + 1)
    selecetd_stones.pop()
    backtrack(idx + 1, cnt)


backtrack(0, 0)
print(ans)

# 8/27 - 1: 조합 전개하는 부분 다시 봐라.. 그새 안했다고 까먹었네
