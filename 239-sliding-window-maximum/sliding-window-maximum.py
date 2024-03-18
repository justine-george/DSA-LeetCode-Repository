class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        q = collections.deque()

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # window is formed
            if r + 1 >= k:
                if l > q[0]:
                    q.popleft()
                l += 1
                res.append(nums[q[0]])

        return res