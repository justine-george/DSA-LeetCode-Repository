class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # monotonic decreasing queue
        queue = deque([])

        # keep the monotonicity
        l, r = 0, 0
        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # remove index l from left if exists
            if l > queue[0]:
                queue.popleft()
            
            if r + 1 >= k:
                # left end is the max
                res.append(nums[queue[0]])
                l += 1
            r += 1
        
        return res