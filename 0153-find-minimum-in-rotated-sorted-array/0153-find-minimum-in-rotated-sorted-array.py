class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        minNum = nums[0]
        while left <= right:
            if nums[left] <= nums[right]:
                minNum = min(minNum, nums[left])
            
            mid = int((left + right) / 2)
            
            minNum = min(minNum, nums[mid])
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minNum