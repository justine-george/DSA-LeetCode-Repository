class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # dp
        # recognize base case -> by default, dp[i] = 1
        N = len(arr)
        dp = [1] * N
        self.arr = arr
        sorted_indeces = sorted(range(N), key=self.custom_comparator)
        
        for i in sorted_indeces:
            # forwards
            for j in range(i + 1, N):
                if arr[j] < arr[i] and abs(i - j) <= d:
                    dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break
            # backwards
            for j in range(i - 1, -1, -1):
                if arr[j] < arr[i] and abs(i - j) <= d:
                    dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break
            
        return max(dp)
    
    def custom_comparator(self, n):
            return (self.arr[n])