# TC == O(N) SC == O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len > t_len:
            return False
        i = 0
        k = 0
        while i < s_len and k < t_len:
            if s[i] == t[k]:
                i += 1
                k += 1
            else:
                k += 1
        if i == s_len:
            return True
        else:
            return False


import bisect as bi
from collections import defaultdict


# TC == O(KlogM) SC == O(N) / if we iterate this with many many s to same t
class SolutionV2:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = defaultdict(list)
        for i, c in enumerate(t):
            idx[c].append(i)
        prev = 0
        for i, c in enumerate(s):
            j = bi.bisect_left(
                idx[c], prev
            )  # 현재 문자 c의 인덱스 리스트에서 prev보다 크거나 같은 첫 번째 위치를 찾습니다.
            if j == len(idx[c]):
                return False
            prev = idx[c][j] + 1
        return True


potato = SolutionV2()
res = potato.isSubsequence("abc", "adffsbdsgsc")
print(res)
