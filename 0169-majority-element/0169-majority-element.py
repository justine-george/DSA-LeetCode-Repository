class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Magic
        # T: O(n), S: O(1)
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

        # # Magic
        # # T: O(n), S: O(1)
        # # Same code as the one above, but longer
        # res, count = nums[0], 0
        # for i in range(1, len(nums)):
        #     if nums[i] != res:
        #         if count == 0:
        #             res = nums[i]
        #         else:
        #             count -= 1
        #     else:
        #         count += 1

        # return res