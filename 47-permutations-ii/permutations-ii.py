class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count_map = Counter(nums)
        res = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for key in count_map:
                if count_map[key] > 0:
                    perm.append(key)
                    count_map[key] -= 1

                    dfs()

                    count_map[key] += 1
                    perm.pop()

        dfs()
        return res