class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0] * N
        dp[-1] = nums[-1]

        # store indices of the dp array
        dq = deque([N - 1])

        '''
        [1,  -1,  -2,  4, -7, 3]
        [7    6    5   7  -4  3]
        '''
        for i in range(N - 2, -1, -1):
            while dq and dq[0] > i +  k:
                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            
            dq.append(i)

        return dp[0]