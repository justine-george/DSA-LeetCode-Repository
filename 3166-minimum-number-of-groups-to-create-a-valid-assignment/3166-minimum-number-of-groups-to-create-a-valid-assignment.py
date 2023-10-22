class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cMap = Counter(nums)

        if len(cMap) == 1:
            return 1

        def search(i):
            ans = 0
            for key in cMap:
                rem = cMap[key] % i
                if rem > cMap[key] // i:
                    return 0
                ans += ceil(cMap[key] / (i + 1))

            return ans

        min_val, max_val = 1, min(cMap.values())
        res = float('inf')
        for i in range(min_val, max_val + 1):
            val = search(i)
            if val:
                res = min(res, val)
        return res