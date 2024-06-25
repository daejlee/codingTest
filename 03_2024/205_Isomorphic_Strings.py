# TC == O(N) SC == O(N)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t) == 1:
            return True
        dic_s = {}
        dic_t = {}
        for i in range(len(s)):
            if s[i] in dic_s:
                dic_s[s[i]] += 1
            else:
                dic_s[s[i]] = 1
            if t[i] in dic_t:
                dic_t[t[i]] += 1
            else:
                dic_t[t[i]] = 1
        lst_s = list(dic_s.values())
        lst_t = list(dic_t.values())
        res1 = lst_t == lst_s
        dic_s = {}
        dic_t = {}
        idx_s = 0
        idx_t = 0
        conn_s = 1
        conn_t = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                dic_s[idx_s] = conn_s
                conn_s = 1
                idx_s += 1
            else:
                conn_s += 1
            if t[i] != t[i - 1]:
                dic_t[idx_t] = conn_t
                conn_t = 1
                idx_t += 1
            else:
                conn_t += 1
        lst_s = list(dic_s.values())
        lst_t = list(dic_t.values())
        res2 = lst_t == lst_s
        return res1 and res2


# TC == O(N) SC == O(N)
class SolutionV2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = [0] * 256
        m2 = [0] * 256
        n = len(s)
        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
        return True
