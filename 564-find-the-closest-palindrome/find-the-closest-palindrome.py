class Solution:
    def nearestPalindromic(self, n: str) -> str:
        '''
        12345: 
        candidates:
            12321
            12[2]21
            12[4]21
            9999
            100001

        '''

        is_even = len(n) % 2 == 0

        mid = len(n) // 2 - 1 if is_even else len(n) // 2
        firstHalf = int(n[:mid + 1])

        candidates = []

        def half_to_palindrome(firstHalf, is_even):
            strFirst = str(firstHalf)
            strSecond = ''
            if is_even:
                strSecond = strFirst[::-1]
            else:
                strSecond = strFirst[:-1][::-1]
            
            return int(strFirst+strSecond)



        candidates.append(half_to_palindrome(firstHalf, is_even))
        candidates.append(half_to_palindrome(firstHalf + 1, is_even))
        candidates.append(half_to_palindrome(firstHalf - 1, is_even))
        candidates.append(10 ** (len(n) - 1) - 1)
        candidates.append(10 ** len(n) + 1)

        diff = float('inf')
        res = 0
        n_int = int(n)
        for candidate in candidates:
            if candidate == n_int:
                continue
            
            if abs(candidate - n_int) < diff:
                res = candidate
                diff = abs(candidate - n_int)
            elif abs(candidate - n_int) == diff:
                res = min(res, candidate)
        
        return str(res)