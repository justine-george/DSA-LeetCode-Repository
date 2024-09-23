class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # T: O(n), S: O(n)
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
        
        # # O(n), O(n) solution
        # visited = set()
        # for n in nums:
        #     if n in visited:
        #         return True
        #     visited.add(n)
        # return False

        # # O(nlogn), O(1) solution
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False