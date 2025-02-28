# places를 순회하며 place 하나당 2차원 배열을 생성
# 0, 0부터 시작하여 완전탐색
# P가 걸리면 x, y 각각 +방향으로 다른 지원자랑 가까운지 탐색
#   거리두기 실패시 0 리턴
#   성공시 continue


def check_dist(place, x, y):
    for i in range(1, 3):
        if x + i >= 5:
            break
        if place[x + i][y] == "P":
            if i == 1:
                return False
            elif i == 2 and place[x + 1][y] != "X":
                return False
    for i in range(1, 3):
        if y + i >= 5:
            break
        if place[x][y + i] == "P":
            if i == 1:
                return False
            elif i == 2 and place[x][y + 1] != "X":
                return False
    if x + 1 < 5 and y + 1 < 5 and place[x + 1][y + 1] == "P":
        if place[x + 1][y] != "X" or place[x][y + 1] != "X":
            return False
    if x - 1 >= 0 and y + 1 < 5 and place[x - 1][y + 1] == "P":
        if place[x - 1][y] != "X" or place[x][y + 1] != "X":
            return False
    return True


def solution(places):
    answer = []
    for place in places:
        is_done = False
        for i in range(5):
            for j in range(5):
                x, y = i, j
                if place[x][y] == "P":
                    is_distanced = check_dist(place, x, y)
                    if is_distanced == False:
                        answer.append(0)
                        is_done = True
                        break
            if is_done:
                break
        if is_done == False:
            answer.append(1)

    return answer
