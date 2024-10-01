class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # T: O(nk), S: O(n)
        q = deque()
        for i in range(1, n + 1):
            q.append(i)

        for _ in range(n - 1):
            # shift k - 1 times
            for i in range(k - 1):
                val = q.popleft()
                q.append(val)
            
            # remove kth
            q.popleft()

        # last one remains is the winner
        return q.popleft()