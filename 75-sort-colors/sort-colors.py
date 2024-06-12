class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # r 0
        # w 1
        # b 2

        # dutch flag sort
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



