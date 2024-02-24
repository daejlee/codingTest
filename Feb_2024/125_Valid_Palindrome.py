# TC == O(n+m) SC == O(m)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in range(len(s)):
            if s[i].isalnum() and s[i].isupper():
                res += s[i].lower()
            elif s[i].isalnum():
                res += s[i]
        for i in range(len(res) // 2):
            l = res[i]
            r = res[-i - 1]
            if l != r:
                return False
        return True


# TC == O(n) SC == O(1)
class SolutionV2:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and s[l].isalnum() == False:
                l += 1
            while r > l and s[r].isalnum() == False:
                r -= 1
            if l > r or s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
