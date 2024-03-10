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


potato = Solution()
res = potato.isSubsequence("abc", "adffsbdsgsc")
print(res)
