class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n), O(n) solution
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False

        # # O(nlogn), O(1) solution
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False