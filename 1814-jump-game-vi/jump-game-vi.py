class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # Initialize the dp array with the same value of nums for last element
        dp = [0] * N
        dp[-1] = nums[-1]

        # Deque to store indices, starting with the last index
        dq = deque([N - 1])

        '''
        [1,  -1,  -2,  4, -7, 3]
        [7    6    5   7  -4  3]
        '''
        for i in range(N - 2, -1, -1):
            # Remove indices from deque which are out of current range [i + 1, i + k]
            while dq and dq[0] > i +  k:
                dq.popleft()
            
            # Compute the maximum score for current position
            dp[i] = nums[i] + dp[dq[0]]

            # Maintain the deque so that it stores indices in decreasing order of dp values
            # Remove elements from the back if they are less than or equal to the current score
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            
            dq.append(i)

        # dp[0] holds the maximum score from the first to the last index
        return dp[0]