n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
ans = 0
visited = {}


# 현재 좌표에서 자신의 행 끝까지 순회하며 다음 열의 같은 행 좌표로 백트레킹 진행
def proceed(curr_row):
    global ans
    if curr_row == n:
        ans = max(ans, sum(visited.values()))
        return
    for i in range(n):
        if i in visited.keys():
            continue
        visited[i] = mat[curr_row][i]
        proceed(curr_row + 1)
        del visited[i]


proceed(0)
print(ans)

# 딕셔너리 쓰는 법 좀 기억하자
