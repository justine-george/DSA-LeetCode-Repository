class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        res = []
        perms = self.permute(nums[1:])
        # insert nums[0] at every position for each p in perms
        for p in perms:
            for i in range(len(p) + 1):
                new_p = p[:i] + [nums[0]] + p[i:]
                res.append(new_p)
        return res
