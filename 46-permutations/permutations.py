class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm) + 1):
                    # insert num at every possible position
                    new_perm = perm[:i] + [num] + perm[i:]
                    print(new_perm)
                    new_res.append(new_perm)
            res = new_res
        return res