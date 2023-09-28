class Solution:
    def trap(self, height: List[int]) -> int:
        # # 2 pointer, T: O(n), S: O(1)
        # if not height:
        #     return 0
        
        # l, r = 0, len(height) - 1
        # lMax, rMax = height[l], height[r]
        # res = 0

        # while l < r:
        #     if lMax < rMax:
        #         l += 1
        #         lMax = max(lMax, height[l])
        #         res += lMax - height[l]
        #     else:
        #         r -= 1
        #         rMax = max(rMax, height[r])
        #         res += rMax - height[r]
        
        # return res

        # store indeces
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                index = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[stack[-1]], height[i]) - height[index]
                res += (distance * bounded_height)
            stack.append(i)
        
        return res