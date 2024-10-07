class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # max heap
        h = [(-nums[0], 0)]

        for i in range(1, N):
            while h[0][1] < i - k:
                heappop(h)
            max_so_far = -h[0][0]
            current_score = max_so_far + nums[i]
            heappush(h, (-current_score, i))
            if i == N - 1:
                return (max_so_far + nums[i])

        return nums[0]

        # # Deque to store indices, starting with the first index
        # dec_q = deque([0])

        # k += 1 # size of sliding window

        # for i in range(1, N):
        #     # Remove indices from deque which are out of current range [i + 1, i + k]
        #     while dq and dq[0] > i +  k:
        #         dq.popleft()
            
        #     # Compute the maximum score for current position
        #     dp[i] = nums[i] + dp[dq[0]]

        #     # Decreasing monotonic queue to get max of sliding window
        #     # Maintain the deque so that it stores indices in decreasing order of dp values
        #     # Remove elements from the back if they are less than or equal to the current score
        #     while dq and dp[i] >= dp[dq[-1]]:
        #         dq.pop()
            
        #     dq.append(i)

        # # dp[0] holds the maximum score from the first to the last index
        # return dp[0]