class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # r 0
        # w 1
        # b 2

        # # counting sort since we know max range
        # count_map = Counter(nums)
        # order = [0, 1, 2]
        # i = 0
        # for o in order:
        #     while count_map[o] > 0:
        #         nums[i] = o
        #         i += 1
        #         count_map[o] -= 1

        # single pass and S: O(1) - dutch flag sort
        zero, it, two = 0, 0, len(nums) - 1
        while it <= two:
            if nums[it] == 0:
                nums[it], nums[zero] = nums[zero], nums[it]
                it += 1
                zero += 1
            elif nums[it] == 2:
                nums[it], nums[two] = nums[two], nums[it]
                two -= 1
            else:
                it += 1