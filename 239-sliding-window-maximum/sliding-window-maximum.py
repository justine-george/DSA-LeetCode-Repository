class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, 0
        q = collections.deque()

        for r in range(len(nums)):
            # to keep monotonic decreasing behavior (q[0] should be the max)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # if out of bounds, remove left
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
        return res