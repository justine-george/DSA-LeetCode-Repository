class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        res = 0
        dp = [0] * len(books)
        stack = []

        f = lambda i: books[i] - i

        for i, book in enumerate(books):
            while stack and stack[-1][0] >= f(i):
                stack.pop()
            
            j = stack[-1][1] if stack else -1

            first = book
            last = book - (i - (j + 1))
            count = i - j

            if last < 0:
                dp[i] = (first * (first + 1) // 2)
            else:
                dp[i] = (dp[j] if j >= 0 else 0) + ((first + last) * count // 2)
            
            res = max(res, dp[i])
            stack.append((f(i), i))
        
        return res