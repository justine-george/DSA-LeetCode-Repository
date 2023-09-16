class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        map = [{} for i in range(len(nums))]
        
        res = 2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if diff in map[i]:
                    map[j][diff] = map[i][diff] + 1
                else:
                    map[j][diff] = 2
                res = max(res, map[j][diff])
        
        return res