class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        global_min = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                global_min = min(global_min, nums[l])
                break
            
            mid = l + (r - l) // 2
            global_min = min(global_min, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return global_min