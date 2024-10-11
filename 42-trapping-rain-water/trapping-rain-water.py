class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N <= 2:
            return 0

        l, r = 0, N - 1
        max_left, max_right = height[l], height[r]
        total_water = 0
        while l < r:
            if max_left < max_right:
                l += 1
                water_collected = max_left - height[l]
                if water_collected > 0:
                    total_water += water_collected
                max_left = max(max_left, height[l])
            else:
                r -= 1
                water_collected = max_right - height[r]
                if water_collected > 0:
                    total_water += water_collected
                max_right = max(max_right, height[r])

        return total_water

        '''
        N = len(height)
        if N <= 2:
            return 0

        # calculate max height to the left and right
        max_height_to_left_of = {0: -1}
        max_height_to_right_of = {N - 1: -1}

        for i in range(1, N):
            max_height_to_left_of[i] = max(max_height_to_left_of[i - 1], height[i - 1])
        
        for i in range(N - 2, -1, -1):
            max_height_to_right_of[i] = max(max_height_to_right_of[i + 1], height[i + 1])

        total_water_collected = 0
        for i in range(1, N - 1):
            cur_height = min(max_height_to_left_of[i], max_height_to_right_of[i])
            cur_water = cur_height - height[i]
            if cur_water > 0:
                total_water_collected += cur_water

        return total_water_collected
        '''