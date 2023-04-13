class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        
        for n in nums:
            # if it doesn't have a left neighbor => start of a sequence
            if (n - 1) not in numSet:
                # new sequence
                len = 1
                temp = n
                while (temp + 1) in numSet:
                    temp += 1
                    len += 1
                maxLen = max(maxLen, len)
        
        return maxLen
                    