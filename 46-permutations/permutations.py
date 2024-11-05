class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        perm = []
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
            
            for key in count:
                if count[key] > 0:
                    perm.append(key)
                    count[key] -= 1

                    dfs()

                    perm.pop()
                    count[key] += 1

        dfs()
        return res