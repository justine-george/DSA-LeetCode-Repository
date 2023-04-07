class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minNum = nums[0]
        while left <= right:
            if nums[left] <= nums[right]:
                minNum = minNum if minNum < nums[left] else nums[left]
                break
                
            mid = (left + right) // 2
            minNum = minNum if minNum < nums[mid] else nums[mid]

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minNum