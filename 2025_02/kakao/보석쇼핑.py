# gems 배열에서 set으로 보석 종류를 파악

import sys
from collections import defaultdict


def solution(gems):
    min_gems = sys.maxsize
    len_gems = len(gems)
    n_gems = len(set(gems))
    end = 0
    basket = defaultdict(lambda: 0)
    for start, gem in enumerate(gems):
        while len(basket) < n_gems and end < len_gems:
            basket[gems[end]] += 1
            end += 1
        if len(basket) == n_gems:
            if min_gems > end - start:
                min_gems = end - start
                result = [start + 1, end]
        basket[gem] -= 1
        if basket[gem] == 0:
            del basket[gem]
    return result


# 접근 실패. DP로 풀려다가 실패했음.
# 투 포인터로 범위 조정하면서 구하기
