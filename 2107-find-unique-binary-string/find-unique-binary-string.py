class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numsSet = set(nums)
        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return res if res not in numsSet else None
            
            cur[i] = '1'
            res = backtrack(i + 1, cur)
            if res: return res
            cur[i] = '0'
        
            res = backtrack(i + 1, cur)
            if res: return res

        return backtrack(0, ['0' for n in nums])
