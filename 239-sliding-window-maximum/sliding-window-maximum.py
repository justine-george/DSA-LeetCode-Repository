class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # res = [0] * (n - k + 1)
        res = []
        l, r = 0, 0
        q = collections.deque()

        while r < len(nums):
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
            r += 1
            
        return res