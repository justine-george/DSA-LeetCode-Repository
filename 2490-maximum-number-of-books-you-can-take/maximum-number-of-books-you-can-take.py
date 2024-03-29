class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        """
        # index: count of books
        4: books[i]
        3: (books[i] - 1) or greater books should be there
        2: (books[i] - 2) or greater books should be there
        1: (books[i] - 3) or greater books should be there
        ..
        j: (books[i] - (i - j)) or greater books should be there
        
        so, at index j( < i), if books[j] < books[i] - (i - j), it means there isn't enough books here.
        ie. books[j] - j < books[i] - i is the breaking condition.
        => [j + 1, i] is an AP. (calculate sum in O(1))
        AP sum = 1/2(first+last)*number of elems

        dp[i] = max # of books we can take from all the shelves [0, i], when we take books[i] from ith shelf

        [j + 1, i] -> calculateSum(j + 1, i)
        but what is [0, j]? it is actually dp[j]
        => dp[i] = (dp[j] if j exists else 0) + calculateSum(j + 1, i) if last is not negative, else
           dp[i] = calculateSum(0, i) ie. book[i]*(book[i] + 1)//2
        """
        #  T: O(n), S: O(n)
        res = 0
        dp = [0] * len(books)
        stack = []

        f = lambda i: books[i] - i

        for i, book in enumerate(books):
            # because index i will run out of items first
            while stack and stack[-1][0] >= f(i):
                stack.pop()

            j = stack[-1][1] if stack else -1

            first = book
            last = book - (i - (j + 1))

            if last < 0:
                dp[i] = first * (first + 1) // 2
            else:
                count = i - j
                dp[i] = (dp[j] if j >= 0 else 0) + ((first + last) * count // 2)

            stack.append((f(i), i))
            res = max(res, dp[i])
        
        return res