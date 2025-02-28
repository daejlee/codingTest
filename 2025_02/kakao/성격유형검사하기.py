# A, N, C, F, M, J, R, T 딕셔너리 생성
# survey 순회하면서 딕셔너리에 값 더하기
# 점수 높은 순서대로 성격유형 생성. 같으면 사전순


def solution(survey, choices):
    answer = ""
    dict = {"R": 0, "T": 0, "C": 0, "F": 0, "M": 0, "J": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        if choices[i] > 4:
            dict[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            dict[survey[i][0]] += 4 - choices[i]
    pair = []
    str_pair = []
    print(dict)
    for key, value in dict.items():
        pair.append([value, key])
        str_pair.append([key, value])
        if len(pair) == 2:
            pair.sort()
            str_pair.sort()
            if pair[0][0] == pair[1][0]:
                answer += str(str_pair[0][0])
            else:
                answer += str(pair[1][1])
            pair = []
            str_pair = []
    return answer


# 20분
