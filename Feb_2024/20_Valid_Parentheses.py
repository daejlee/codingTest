from collections import deque


# TC == O(n) SC == O(1)
class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        for i in range(len(s)):
            if s[i] == "(":
                dq.append(")")
            elif s[i] == "{":
                dq.append("}")
            elif s[i] == "[":
                dq.append("]")
            elif len(dq) == 0 or dq.pop() != s[i]:
                return False
        if len(dq):
            return False
        return True
