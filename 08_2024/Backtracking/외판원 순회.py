n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
visited = [[0, 0]] # pos, val
ans = 1000000000

# 0으로 돌아가는 비용까지 더해서 합을 리턴한다.
def get_visited_sum():
    last_stop = visited[-1][0]
    res = mat[last_stop][0]
    if res == 0:
        return 1000000000
    for item in visited:
        res += item[1]
    return res

def is_pass(next_pos):
    for item in visited:
        if item[0] == next_pos:
            return True
    return False

# 마지막 방문한 위치(visited 배열 마지막 원소)에서 다음 위치로 이동한다.
# 백트레킹 한다. 만약 모두 방문했으면 최대값을 업데이트하고 마지막 원소 팝
def visit():
    global ans
    if len(visited) >= n:
        ans = min(ans, get_visited_sum())
        return
    
    curr_pos = visited[-1][0]
    for i in range(n):
        if mat[curr_pos][i] == 0 or is_pass(i) == True:
            continue
        visited.append([i, mat[curr_pos][i]])
        visit()
        visited.pop()

visit()
print(ans)