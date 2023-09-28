class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T: O(n), S: O(n)
        map = {}
        for i, n in enumerate(nums):
            if target - n in map:
                return [map[target - n], i]
            map[n] = i