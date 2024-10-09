from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # T: O(nlogn) solution - patience sorting (think cardgame)
        # # number of the piles give the length of the LIS
        # piles = []
        
        # for num in nums:
        #     # Find the position where `num` would fit in piles
        #     index = bisect_left(piles, num)
        #     if index == len(piles):
        #         piles.append(num)
        #     else:
        #         piles[index] = num

        # return len(piles)

        # if i want to return the LIS
        pile = [nums[0]]
        max_len = 1
        for num in nums[1:]:
            if num > pile[-1]:
                pile.append(num)
                max_len += 1
            else:
                # index = bisect_left(pile, num)
                # pile[index] = num
                l, r = 0, len(pile) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if pile[mid] < num:
                        l = mid + 1
                    else:
                        r = mid - 1
                pile[l] = num
        print(pile)
        return max_len

        '''
        # better options
        # T: O(n**2), S: O(n)
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        
        # better options
        # T: O(n**2), S: O(n)
        @lru_cache(maxsize=None)
        def dfs(i):
            max_len = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, 1 + dfs(j))

            return max_len
        
        return max(dfs(i) for i in range(len(nums)))
        
        # worst option
        # T: O(n**2), S: O(n**2)
        @cache
        def dfs(i, prev_added_idx):
            if i == len(nums):
                return 0

            # skip
            max_length = dfs(i + 1, prev_added_idx)

            # take
            if prev_added_idx == -1 or nums[i] > nums[prev_added_idx]:
                max_length = max(max_length, 1 + dfs(i + 1, i))
            
            return max_length
        
        return dfs(0, -1)
        '''