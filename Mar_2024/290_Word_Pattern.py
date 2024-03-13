class Solution:
    # SC == O(N) TC == O(N)
    def wordPattern(self, pattern: str, s: str) -> bool:
        w_list = s.split(" ")
        p_dict = {}
        if len(w_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            c = pattern[i]
            val = p_dict.get(c)
            if val == None:
                if w_list[i] in p_dict.values():
                    return False
                else:
                    p_dict[c] = w_list[i]
            elif val != w_list[i]:
                return False
        return True

    def wordPatternV2(self, pattern: str, s: str):
        p = pattern
        t = s.split()
        return map(p.find, p) == map(t.index, t)

    def wordPatternV3(self, pattern: str, s: str):
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return f(pattern) == f(str.split())
