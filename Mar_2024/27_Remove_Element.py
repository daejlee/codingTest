# TC == O(N) / SC == O(1)
# I understood the concept of two-pointers but my dumbass couldn't make this simple loop.


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
