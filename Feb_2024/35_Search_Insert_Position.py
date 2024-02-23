class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        size = len(nums)
        if size % 2:
            pivot = size // 2
        else:
            pivot = size // 2 - 1
        while True:
            size //= 2
            if size == 0:
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
