# Well, this is just simple fibonacci !!
memo = [0] * 46


# TC == O(n) SC == O(n), Recursion + Top-down / Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            memo[n] = 2
        elif n <= 1:
            memo[n] = 1
        elif memo[n]:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return memo[n]


# TC == O(n) SC == O(n), Iteration + Bottom-up / Tabulation
class SolutionV2:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]


# TC == O(n) SC == O(2), Iteration + Bottom-up / Space Optimization
class SolutionV3:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr


# Summary: In DP, we just need two things. Initial value and Recurrence relation.
# Think: What is difference between Memoization and Tabulation?
