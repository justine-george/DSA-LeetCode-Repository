class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        """
        # index: count
        4: books[i]

        3: books[i] - 1 or greater books should be there
        2: books[i] - 2
        1: books[i] - 3
        
        so, at index j( < i), if books[j] < books[i] - (i - j), it means there isn't enough books here.
        ie. books[j] - j < books[i] - i is the breaking condition.
        => [j + 1, i] is an AP. (calculate sum in O(1))
        AP sum = 1/2(first+last)*number of elems

        dp[i] = max # of books we can take from all the shelves [0, i], when we take books[i] from ith shelf

        [j + 1, i] -> calculateSum(j + 1, i)
        but what is [0, j]? it is actually dp[j]
        => dp[i] = dp[j] + calculateSum(j + 1, i) if j exists, else
        dp[i] = calculateSum(0, i)
        """
        #  T: O(n), S: O(n)
        res = 0
        dp = [0] * len(books)
        stack = []

        f = lambda i: books[i] - i

        for i, book in enumerate(books):
            while stack and stack[-1][0] >= f(i):
                stack.pop()

            j = stack[-1][1] if stack else -1

            if book - (i - (j + 1)) < 0:
                dp[i] = book * (book + 1) // 2
            else:
                first = book
                last = book - (i - (j + 1))
                count = i - j
                dp[i] = (dp[j] if j >= 0 else 0) + ((first + last) * count // 2)

            stack.append((f(i), i))
            res = max(res, dp[i])
        
        return res




