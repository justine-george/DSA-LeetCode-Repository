class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # r 0
        # w 1
        # b 2

        # counting sort since we know max range
        count_map = defaultdict(int)
        for n in nums:
            count_map[n] += 1
        
        order = [0, 1, 2]
        i = 0
        for o in order:
            while count_map[o] > 0:
                nums[i] = o
                i += 1
                count_map[o] -= 1

        # for i in range(len(nums)):
        #     if count_map[0] > 0:
        #         nums[i] = 0
        #         count_map[0] -= 1
        #     elif count_map[1] > 0:
        #         nums[i] = 1
        #         count_map[1] -= 1
        #     else:
        #         nums[i] = 2
        #         count_map[2] -= 1

        # # dutch flag sort
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