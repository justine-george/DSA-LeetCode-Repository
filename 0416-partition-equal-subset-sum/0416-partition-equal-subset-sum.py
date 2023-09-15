class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2:
            return False

        targetSum = total // 2
        nums.sort(reverse=True)
        if nums[0] > targetSum:
            return False

        memo = {}

        def backtrack(i, subsetSum):
            if i == len(nums):
                return False
            
            if (i, subsetSum) in memo:
                return memo[(i, subsetSum)]
            
            if subsetSum == targetSum:
                return True

            # Include the current number in the subset
            if subsetSum + nums[i] <= targetSum and backtrack(i + 1, subsetSum + nums[i]):
                memo[(i, subsetSum)] = True
                return True
            
            # Exclude the current number from the subset
            if backtrack(i + 1, subsetSum):
                memo[(i, subsetSum)] = True
                return True
            
            memo[(i, subsetSum)] = False
            return False

        return backtrack(0, 0)
