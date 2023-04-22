class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=wjYnzkAhcNk
        # convert to linkedlist cycle detection problem
        # floyd's cycle detection - find out start of the cycle
        # T: O(n), S: O(1)
        
        # 0 because it is never a part of the cycle
        # numbers are in the range [1, n] inclusive
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]    
            if slow == fast:
                break
        
        slow2 = 0
        # now increment slow and slow2 until they intersect
        # this will be the duplicate (start of the cycle)
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow