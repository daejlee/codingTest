# 종류를 키 값으로 갖는 해시맵을 생성
# 해시맵을 순회하면서 가능한 조합의 경우의 수를 구함
is_checked = []
test = {}
ans = 0


# 가능한 경우의 수를 모두 포함하는 2차원 배열을 반환
def get_comb(idx, cloth_list):
    global ans

    if idx >= len(cloth_list):
        if len(is_checked) > 0 and is_checked not in test.values():
            test[ans] = is_checked.copy()
            ans += 1
        return

    for cloth in cloth_list[idx]:
        if cloth in is_checked:
            continue
        is_checked.append(cloth)
        get_comb(idx + 1, cloth_list)
        is_checked.pop()
        get_comb(idx + 1, cloth_list)


def solution(clothes):
    dict = {}
    global ans

    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]].append(cloth[0])
        else:
            dict[cloth[1]] = [cloth[0]]
    cloth_list = list(dict.values())

    get_comb(0, list(cloth_list))
    print(ans)
    return ans


"""
2/19 해시맵을 이용한 조합 문제

시간 초과 났음
수학적 접근을 못한것 같다.
문제가 간단했다. 각 부위마다의 아이템의 갯수를 세서, (ex. 3개의 상의, 2개의 하의, 1개의 모자)
각 부위마다의 아이템의 갯수에 1을 더한 값을 모두 곱하고, 1을 뺀다.
(더하는 이유는 해당 부위의 아이템을 입지 않는 경우도 포함하기 위함, 아무것도 안 입는 경우는 1을 빼는)

조합을 구해야 한다는 생각에 사로잡혀서 이전에 알고 있던 방식에 갇혀버린 것 같다.
여러 문제를 풀어보면 해결 될 일이라고 생각.
그리고 해시맵을 조금 풀면서 느끼는 건데, 난이도가 높아지면 사실 해시맵 자체보다는 응용 개념이 중요한 듯.

[simple answer]
def solution(clothes):
    dict_clothes = {}
    for val, key in clothes:
        if key in dict_clothes.keys():
            dict_clothes[key] += 1
        else:
            dict_clothes.update[key] = 1
    answer = 1
    for val_cnt in dict_clothes.values():
        answer *= val_cnt + 1
    return answer - 1
"""
