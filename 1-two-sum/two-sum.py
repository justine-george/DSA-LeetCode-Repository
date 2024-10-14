class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, n in enumerate(nums):
            if target - n in seen_map:
                return [i, seen_map[target - n]]
            seen_map[n] = i