class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        
        targetSum = sum(nums) / k
        if nums[0] > targetSum:
            return False
        
        used = [False] * len(nums)
        
        def backtrack(index, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == targetSum:
                return backtrack(0, k - 1, 0)
            
            for j in range(index, len(nums)):
                if used[j] or subsetSum + nums[j] > targetSum or (j > 0 and nums[j] == nums[j - 1] and not used[j - 1]):
                    continue
                
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            
            return False
        
        return backtrack(0, k, 0)
