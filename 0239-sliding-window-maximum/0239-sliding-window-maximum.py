class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # initialize a monotonic decreasing queue, first window
        queue = deque([])
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])

        # keep the monotonicity
        l = 0
        for r in range(k, len(nums)):
            # remove index l from left if exists
            if queue[0] == l:
                queue.popleft()
            l += 1

            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            
            # left end is the max
            res.append(nums[queue[0]])
        
        return res