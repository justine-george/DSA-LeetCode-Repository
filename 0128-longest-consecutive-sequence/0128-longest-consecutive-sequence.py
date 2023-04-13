class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # T: O(n), S: O(n)
        numSet = set(nums)
        maxLen = 0
        
        for n in nums:
            # if it doesn't have a left neighbor => start of a sequence
            if (n - 1) not in numSet:
                # new sequence
                len = 1 # length of this sequence
                # if it has a right neighbor => next element of the sequence exists
                while (n + len) in numSet:
                    len += 1
                maxLen = max(maxLen, len)
        
        return maxLen
                    