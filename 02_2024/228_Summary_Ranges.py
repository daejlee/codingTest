# TC == O(n), SC == O(len(res) + 2)


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        if len(nums) == 0:
            return res
        elif len(nums) == 1:
            res.append(str(nums[0]))
            return res
        tail = head = nums[0]
        for i in range(1, len(nums)):
            tail = nums[i - 1]
            if nums[i] - nums[i - 1] != 1:
                if head == tail:
                    res.append(str(head))
                else:
                    res.append(str(head) + "->" + str(tail))
                head = nums[i]
        tail = nums[-1]
        if head == tail:
            res.append(str(head))
        else:
            res.append(str(head) + "->" + str(tail))
        return res
