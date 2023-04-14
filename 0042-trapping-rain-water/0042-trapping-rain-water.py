class Solution:
    def trap(self, height: List[int]) -> int:
        # T: O(n), S: O(n)
        n = len(height)
        maxLeftHeight = [0] * n
        maxRightHeight = [0] * n
        
        # calculate maxLeftHeight
        maxH = 0
        for i in range(1, n):
            maxH = max(maxH, height[i - 1])
            maxLeftHeight[i] = maxH
        
        # calculate maxRightHeight
        maxH = 0
        for i in range(n - 2, -1, -1):
            maxH = max(maxH, height[i + 1])
            maxRightHeight[i] = maxH
        
        # calculate amount of trapped water
        totalWater = 0
        for i in range(n):
            curWater = min(maxLeftHeight[i], maxRightHeight[i]) - height[i]
            curWater = 0 if curWater <= 0 else curWater
            totalWater += curWater
        
        return totalWater