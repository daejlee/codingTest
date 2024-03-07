# TC == O(N) SC == O(1)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        k = 1
        i = 1
        while i < n:
            if nums[i] == nums[i - 1]:
                while nums[i] == nums[i - 1]:
                    if i == n - 1:
                        return k
                    i += 1
                nums[k] = nums[i]
            else:
                nums[k] = nums[i]
            i += 1
            k += 1
        return k


# TC == O(N) SC == O(1) / in-place array problem -> WE NEED TO SIMPLIFY THINGS!!!!
class SolutionV2:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
