class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        valSet = set(nums)
        if len(valSet) != len(nums):
            return True
        else:
            return False