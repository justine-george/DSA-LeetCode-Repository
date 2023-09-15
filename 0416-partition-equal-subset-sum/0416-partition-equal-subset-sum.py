class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        nums.sort(reverse=True)
        
        targetSum = sum(nums) / 2
        if nums[0] > targetSum:
            return False
        
        used = [False] * len(nums)
        memo = {}
        
        def backtrack(i, k, subsetSum):
            if (i, k, subsetSum) in memo:
                return memo[(i, k, subsetSum)]
            
            if k == 0:
                memo[(i, k, subsetSum)] = True
                return True
            
            if subsetSum == targetSum:
                # memo[(i, k, subsetSum)] = backtrack(0, k - 1, 0)
                # return memo[(i, k, subsetSum)]
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > targetSum or (j > 0 and nums[j] == nums[j - 1] and not used[j - 1]):
                    continue
                
                used[j] = True
                if backtrack(j, k, subsetSum + nums[j]):
                    memo[(j, k, subsetSum + nums[j])] = True
                    return True
                used[j] = False
            
            memo[(i, k, subsetSum)] = False
            return False
        
        return backtrack(0, 2, 0)