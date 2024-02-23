# TC == O(logn) SC == O(1)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        size = len(nums)
        if size % 2:
            pivot = size // 2
        else:
            pivot = size // 2 - 1
        while True:
            size //= 2
            if size == 0:  # This is post processing
                if target > nums[pivot]:
                    return pivot + 1
                elif pivot == 0:
                    return pivot
                elif target <= nums[pivot - 1]:
                    return pivot - 1
                else:
                    return pivot
            if target > nums[pivot]:
                pivot += size
                if pivot >= len(nums):
                    pivot = len(nums) - 1
            elif target < nums[pivot]:
                pivot -= size
                if pivot < 0:
                    pivot = 0
            else:
                return pivot


# TC == O(logn) SC == O(1) / conventional binary search. using l, r pointer.
class SolutionV2:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        l = 0
        r = n - 1
        while l < r:
            m = l + (r - l) / 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1
        if nums[l] < target:
            return l + 1
        else:
            return l
