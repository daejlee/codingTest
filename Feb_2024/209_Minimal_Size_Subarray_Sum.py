# TC == O(n^2) SC == O(1) -> Timed Out!!
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        scope = 0
        while scope < len(nums):
            sum = 0
            for i in range(scope + 1):
                sum += nums[i]
            if sum >= target:
                return scope + 1
            for k in range(1, len(nums) - scope):
                sum -= nums[k - 1]
                sum += nums[k + scope]
                if sum >= target:
                    return scope + 1
            scope += 1
        return 0


# TC == O(n) SC == O(1) / Sliding Window and Two-Ponters
# Subarray Questions!
class SolutionV2:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        r = 0
        sum = 0
        n = len(nums)
        min = len(nums) + 1
        while r < n:
            sum += nums[r]
            r += 1
            while sum >= target:
                if min > r - l:
                    min = r - l
                sum -= nums[l]
                l += 1
        if min == len(nums) + 1:
            return 0
        return min


potato = SolutionV2()
res = potato.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(res)
