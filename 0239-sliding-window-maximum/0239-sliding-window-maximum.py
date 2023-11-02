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

        # 0 1 -> nums[1] = 3, now remove index 0 from left if exists
        # 1 -> nums[1] = 3, now remove index 1 from left if exists
        # 4 -> nums[4] = 5, now remove index 2 from left if exists
        # 4 -> nums[4] = 5, now remove index 3 from left if exists
        # 4, 6 -> nums[6] = 6, now remove index 4 from left if exists
        # 6, 7 -> nums[7] = 7, now remove index 5 from left if exists