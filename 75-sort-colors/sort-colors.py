class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # r 0
        # w 1
        # b 2

        # # counting sort with O(1) since we know max range we can use a bounded array
        count_map = [0] * 3
        for n in nums:
            count_map[n] += 1
        order = [0, 1, 2]
        i = 0
        for o in order:
            while count_map[o] > 0:
                nums[i] = o
                i += 1
                count_map[o] -= 1

        # single pass T: O(n) and S: O(1) - dutch flag sort
        # zero, it, two = 0, 0, len(nums) - 1
        # while it <= two:
        #     if nums[it] == 0:
        #         nums[it], nums[zero] = nums[zero], nums[it]
        #         it += 1
        #         zero += 1
        #     elif nums[it] == 2:
        #         nums[it], nums[two] = nums[two], nums[it]
        #         two -= 1
        #     else:
        #         it += 1