# 4행 3열의 가상 키패드 배열이 있다고 가정한다.
# 각 손가락의 위치를 값으로 갖고 있으면서 업데이트 한다.
# 최소 거리를 재서 이동.
# 1, 4, 7은 왼손
# 3, 6, 9는 오른손
# 중간은 더 가까운 손으로


def get_dist(curr, n):
    # print(curr, n)
    l_dict = {
        "1": 0,
        "4": 1,
        "7": 2,
        "3": 0,
        "6": 1,
        "9": 2,
        "2": [0, 1],
        "5": [1, 1],
        "8": [2, 1],
        "0": [3, 1],
    }
    x_diff = abs(curr[0] - l_dict[str(n)][0])
    y_diff = abs(curr[1] - l_dict[str(n)][1])
    return x_diff + y_diff
    return 0


def solution(numbers, hand):
    l_t = [3, 0]
    r_t = [3, 2]
    answer = ""
    for n in numbers:
        dict = {
            "1": 0,
            "4": 1,
            "7": 2,
            "3": 0,
            "6": 1,
            "9": 2,
            "2": [0, 1],
            "5": [1, 1],
            "8": [2, 1],
            "0": [3, 1],
        }
        if n == 1 or n == 4 or n == 7:
            answer += "L"
            l_t[0] = dict[str(n)]
            l_t[1] = 0
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
            r_t[0] = dict[str(n)]
            r_t[1] = 2
        else:
            l_d = get_dist(l_t, n)
            r_d = get_dist(r_t, n)
            if n == 5:
                print(l_t, r_t, l_d, r_d)
            if l_d < r_d:
                l_t = dict[str(n)]
                answer += "L"
            elif l_d > r_d:
                r_t = dict[str(n)]
                answer += "R"
            else:
                if hand == "left":
                    l_t = dict[str(n)]
                    answer += "L"
                if hand == "right":
                    r_t = dict[str(n)]
                    answer += "R"
    return answer


# 35분
