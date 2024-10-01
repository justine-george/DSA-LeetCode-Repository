class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # T: O(nk), S: O(n)
        if n == 1:
            return 1
            
        q = deque()
        for i in range(1, n + 1):
            q.append(i)


        while True:
            # shift k - 1 times
            for i in range(k - 1):
                val = q.popleft()
                q.append(val)
            
            # remove kth
            q.popleft()

            if len(q) == 1:
                return q.popleft()

        # return q.popleft()