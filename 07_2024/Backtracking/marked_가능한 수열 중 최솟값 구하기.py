# 시간 초과 코드..
# def is_possibe(idx, r):
#     global seq
#     if idx + 2 * r > len(seq):
#         return True
#     start_1 = idx
#     start_2 = idx + r
#     for i in range(r):
#         if seq[start_1 + i] != seq[start_2 + i]:
#             return is_possibe(idx, r + 1)
#     return False

# def append_num():
#     global seq, candidates
#     seq_len = len(seq)
#     if seq_len > n: return
#     for i in range(seq_len):
#         if is_possibe(i, 1) == False:
#             return
#     if seq_len == n: # 조건을 통과한 조합을 후보군에 추가한다.
#         candidates.append(seq[:])
#         return
#     for i in range(3):
#         seq.append(nums[i])
#         append_num()
#         seq.pop()

# append_num()
# candidates.sort()
# for i in range(len(candidates[0])):
#     print(candidates[0][i], end='')

n = int(input())
seq = []
nums = [4, 5, 6]


def is_possibe(idx, r):
    global seq
    if idx + 2 * r > len(seq):
        return True
    start_1 = idx
    start_2 = idx + r
    for i in range(r):
        if seq[start_1 + i] != seq[start_2 + i]:
            return is_possibe(idx, r + 1)
    return False


def append_num():
    global seq, candidates
    seq_len = len(seq)
    if seq_len > n:
        return
    for i in range(seq_len):
        if is_possibe(i, 1) == False:
            return

    if seq_len == n:  # 첫 번째 찾은게 답이라는 걸 몰랐다.... 로직 자체는 맞았다.
        for i in range(len(seq)):
            print(seq[i], end="")
        exit()

    for i in range(3):
        seq.append(nums[i])
        append_num()
        seq.pop()


append_num()
