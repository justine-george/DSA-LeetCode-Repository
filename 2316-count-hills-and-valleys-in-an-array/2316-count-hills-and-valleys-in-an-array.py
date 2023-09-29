class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        if len(nums) < 3:  # We need at least 3 numbers to identify a hill or valley.
            return 0

        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i - 1]

            # Check for hill
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                count += 1
            # Check for valley
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                count += 1

        return count