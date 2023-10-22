class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i, j, n = k, k, len(nums)
        res = nums[k]
        cur_min = nums[k]

        while i > 0 or j < n - 1:
            l_num, r_num = nums[i - 1] if i > 0 else 0, nums[j + 1] if j < n - 1 else 0

            if l_num > r_num:
                i -= 1
                cur_min = min(cur_min, nums[i])
            else:
                j += 1
                cur_min = min(cur_min, nums[j])

            res = max(res, cur_min * (j - i + 1))
        
        return res