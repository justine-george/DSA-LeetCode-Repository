class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Recursive
        # T: O(n), S:O(n)
        # def helper(n, k):
        #     if n == 1:
        #         return 0
        #     return (helper(n - 1, k) + k) % n
        # return helper(n, k) + 1

        # # Iterative
        # # T: O(n), S: O(1)
        # res = 0
        # for people in range(2, n + 1):
        #     res = (res + k) % people
        # return res + 1
        
        # T: O(nk), S: O(n)
        q = deque([])
        for i in range(1, n + 1):
            q.append(i)

        while len(q) > 1:
            # shift k - 1 times
            for i in range(k - 1):
                q.append(q.popleft())
            
            # remove kth
            q.popleft()

        # last one remains is the winner
        return q[0]