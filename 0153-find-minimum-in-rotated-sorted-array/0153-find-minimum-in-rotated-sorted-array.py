class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minNum = float("inf")
        
        while left < right:
            
            mid = (left + right) // 2
            minNum = min(minNum, nums[mid])
            
            # right has the min
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # left has the min
            else:
                right = mid - 1
        
        return min(minNum, nums[left])