class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        # 1, 2, ...8
        for i in range(1, len(nums) + 1):
            curNum = nums[i -1]
            if nums[abs(curNum) - 1] < 0:
                res.append(abs(curNum))
            else:
                nums[abs(curNum) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
        
        return res
    
#         [4,3,2,7,8,2,3,1]
        
#         [-4,-3,-2,-7,8,2,-3,-1]
        
#         [3, 2]