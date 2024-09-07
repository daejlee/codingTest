from collections import deque
import math

q = deque()
S = int(input())
# 화면 이모티콘 개수, 클립보드 이모티콘 개수
is_visited = [[False for _ in range(S + 1)] for _ in range(S + 1)]

# 복사 - 붙여넣기 하는 경우
# 하나 삭제하는 경우
# 그냥 붙여넣기 하는 경우
# 위 경우들을 BFS 전개해나가야 한다.

q.append((1, 0, 0))


def q_append(s, clipboard, step):
    if s >= S + 1 or s < 0 or is_visited[s][clipboard] == True:
        return
    q.append((s, clipboard, step))
    is_visited[s][clipboard] = True


while q:
    s, clipboard, step = q.popleft()
    if s == S:
        print(step)
        break

    q_append(s, s, step + 1)  # 복사만 하는 경우
    q_append(s - 1, clipboard, step + 1)  # 하나 삭제
    q_append(s + clipboard, clipboard, step + 1)  # 그냥 붙여넣기

# 9/7 궁금점: 그래프를 완전 탐색하는 것은 알겠지만.. 최솟값을 업데이트해야 하는 것 아닌가? 목표한 S 스텝에 도달하는 경로가 하나 이상이 아닌가..
