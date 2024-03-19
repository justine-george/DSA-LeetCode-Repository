class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = 0
        for n, c in count.items():
            if c == 1:
                return -1
            else:
                # greedy
                # res += (c // 3) + (1 if c % 3 != 0 else 0)
                res += math.ceil(c / 3)

        return res

        # 8: 3 3 2
        # 7: 3 2 2
        # 13: 3 3 3 3 1