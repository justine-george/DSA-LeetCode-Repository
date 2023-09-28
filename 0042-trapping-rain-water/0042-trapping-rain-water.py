class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        water_amount = 0
        
        while l < r:
            # find out the bottleneck
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                water_amount += (lMax - height[l])
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water_amount += (rMax - height[r])
        
        return water_amount
            
