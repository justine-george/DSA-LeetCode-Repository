class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            # start of a sequence
            if n - 1 not in numset:
                len = 1
                while n + len in numset:
                    len += 1
                longest = max(longest, len)
        
        return longest