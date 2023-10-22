class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cMap = Counter(nums)

        if len(cMap) == 1:
            return 1

        # cMap[key] % i -> potential number of group size+1
        # cMap[key] // i-> number of group size

        # (cMap[key] % i) > (cMap[key] // i) means there are not enough number of group size can convert into size+1
        def search(i):
            ans = 0
            for key in cMap:
                q, rem = divmod(cMap[key], i)
                # rem should not exceed the original number of groups
                if rem > q:
                    return 0
                ans += ceil(cMap[key] / (i + 1))

            return ans

        # max group size is {min(cMap.values()), min(cMap.values()) + 1}
        min_val, max_val = 1, min(cMap.values())
        res = float('inf')
        for i in range(min_val, max_val + 1):
            val = search(i)
            if val:
                res = min(res, val)
        return res

        # # Dry run
        # search(7):
        #     ans = 0
        #     for 11
        #         q, rem = 8 // 7, 8 % 7
        #         q, rem = 1, 1
        #         ans += ceil(8/8)

        #         1 1 1 1 1 1 1 . 1