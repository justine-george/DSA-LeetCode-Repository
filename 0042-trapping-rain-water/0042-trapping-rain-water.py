class Solution:
    def trap(self, height: List[int]) -> int:
#         # T: O(n), S: O(n)
#         if not height:
#             return 0
        
#         n = len(height)
#         maxLeftHeight = [0] * n
#         maxRightHeight = [0] * n
        
#         # calculate maxLeftHeight
#         maxH = 0
#         for i in range(1, n):
#             maxH = max(maxH, height[i - 1])
#             maxLeftHeight[i] = maxH
        
#         # calculate maxRightHeight
#         maxH = 0
#         for i in range(n - 2, -1, -1):
#             maxH = max(maxH, height[i + 1])
#             maxRightHeight[i] = maxH
        
#         # calculate amount of trapped water
#         totalWater = 0
#         for i in range(n):
#             curWater = min(maxLeftHeight[i], maxRightHeight[i]) - height[i]
#             curWater = 0 if curWater <= 0 else curWater
#             totalWater += curWater
#         return totalWater
    
        # T: O(n), S: O(1)
        # 2 pointers
        
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            