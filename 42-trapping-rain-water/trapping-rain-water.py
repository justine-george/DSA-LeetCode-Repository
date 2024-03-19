class Solution:
    def trap(self, height: List[int]) -> int:
        # # S: O(1) solution using 2 pointers
        # if not height: return 0

        # n = len(height)
        # l, r = 0, n - 1
        # left_max, right_max = height[l], height[r]
        # res = 0

        # while l < r:
        #     if left_max < right_max:
        #         l += 1
        #         amount = left_max - height[l]
        #         res += (amount if amount > 0 else 0)
        #         left_max = max(left_max, height[l])
        #     else:
        #         r -= 1
        #         amount = right_max - height[r]
        #         res += (amount if amount > 0 else 0)
        #         right_max = max(right_max, height[r])

        # return res

        def get_trapped_water(height):
            n = len(height)
            tallest_to_left, tallest_to_right = [0] * n, [0] * n

            for i in range(1, n):
                tallest_to_left[i] = max(tallest_to_left[i - 1], height[i - 1])
            
            for i in range(n - 2, -1, -1):
                tallest_to_right[i] = max(tallest_to_right[i + 1], height[i + 1])
            
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