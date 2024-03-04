from collections import deque


# TC == O(N) SC == O(N)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        dq = deque()
        while x:
            dq.append(x % 10)
            x //= 10
        if len(dq) == 1:
            return True
        while len(dq) > 1:
            l = dq.pop()
            r = dq.popleft()
            if l != r:
                return False
        return True


# TC == O(N/2) SC == O(1)
class SolutionV2:
    def isPalindrome(self, x: int) -> bool:
        print(x, x % 10)
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return x == reversed_num or x == reversed_num // 10
