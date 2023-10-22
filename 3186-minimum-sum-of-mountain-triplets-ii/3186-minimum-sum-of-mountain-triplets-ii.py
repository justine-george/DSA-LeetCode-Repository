class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        skip = [False] * n
        
        pre = [0] * n # min number to left of this index
        cur_min = nums[0]
        for i in range(1, n):
            cur_min = min(cur_min, nums[i - 1])
            pre[i] = cur_min
            
            if nums[i] <= cur_min:
                skip[i] = True
        
        post = [0] * n # min number to right of this index
        cur_min = nums[-1]
        for i in range(n - 2, 0, -1):
            cur_min = min(cur_min, nums[i + 1])
            post[i] = cur_min
            
            if nums[i] <= cur_min:
                skip[i] = True
            
        for i in range(1, n - 1):
            if not skip[i]:
                res = min(res, pre[i] + nums[i] + post[i])
        
        return res if res != float('inf') else -1
    