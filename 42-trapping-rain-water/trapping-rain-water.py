class Solution:
    def trap(self, height: List[int]) -> int:
        
        def get_trapped_water(height):
            n = len(height)
            tallest_to_left = [0] * n
            tallest_till_now = height[0]
            for i in range(1, n):
                tallest_till_now = max(tallest_till_now, height[i - 1])
                tallest_to_left[i] = tallest_till_now
            
            tallest_to_right = [0] * n
            tallest_till_now = height[n - 1]
            for i in range(n - 2, -1, -1):
                tallest_till_now = max(tallest_till_now, height[i + 1])
                tallest_to_right[i] = tallest_till_now
            
            res = 0
            for i in range(n):
                amount_at_i = min(tallest_to_left[i], tallest_to_right[i]) - height[i]
                res += (amount_at_i if amount_at_i > 0 else 0)

            return res
        
        return get_trapped_water(height)

        # Follow up qn: what if all 0 elevations are holes which leak water?
        # Solution: Split input arr by 0 borders
        # height_list = []
        # temp = []
        # for h in height:
        #     if h == 0:
        #         if temp:
        #             height_list.append(temp)
        #             temp = []
        #     else:
        #         temp.append(h)
        
        # if temp:
        #     height_list.append(temp)
        
        # print(height_list)

        # res = 0
        # for height in height_list:
        #     res += get_trapped_water(height)

        # return res