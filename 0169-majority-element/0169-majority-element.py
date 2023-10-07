class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Magic
        # T: O(n), S: O(1)
        res, count = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] != res:
                if count == 0:
                    res = nums[i]
                else:
                    count -= 1
            else:
                count += 1

        return res