class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()

        for i in range(1, n + 1):
            q.append(i)

        if n == 1:
            return 1

        while True:
            # shift k - 1 times
            for i in range(k - 1):
                val = q.popleft()
                q.append(val)
            
            # remove kth
            q.popleft()

            if len(q) == 1:
                break

        return q.popleft()