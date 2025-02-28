import itertools

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")"]


def get_priority(operator):
    res = itertools.permutations(operator, len(operator))
    return list(res)


def compute(e, p):
    res = ""
    i = 0
    while i < len(e):
        prior = ""
        if e[i] in num:
            if e[i] == "(":
                while e[i] != ")":
                    prior += e[i]
                    i += 1
            else:
                while e[i] in num:
                    prior += e[i]
                    i += 1
        if e[i] == len(e) or e[i] != p:
            if e[i] != p:
                prior += e[i]
            res += prior
            i += 1
            continue
        i += 1
        post = ""
        print(i, e)
        if e[i] in num:
            if e[i] == "(":
                while e[i] != ")":
                    post += e[i]
                    i += 1
            else:
                while i < len(e) and e[i] in num:
                    post += e[i]
                    i += 1
        if p == "-":
            computed = int(prior) - int(post)
            if computed < 0:
                computed = "(" + str(computed) + ")"
        elif p == "+":
            computed = int(prior) + int(post)
        else:
            computed = int(prior) * int(post)
        res += str(computed)
        print(prior, p, post, res, i)
        e = res + e[i:]
        print(e)
        i = len(res)
        break
    print(res)
    return res


def solution(expression):
    operator = []
    answer = 0
    if "+" in expression:
        operator.append("+")
    if "-" in expression:
        operator.append("-")
    if "*" in expression:
        operator.append("*")
    compute("100-110-10", "-")
    # priority_lsts = get_priority(operator)
    # for p_lst in priority_lsts:
    #     local_max = 0
    #     slot = expression
    #     for p in p_lst:
    #         print(slot, p)
    #         slot = compute(slot, p)
    #         print(slot)
    # answer = max(abs(int(slot)), answer)
    return answer


# 시간 초과.. 짜임새 있게 짜지 못했음
