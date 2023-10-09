class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        Calculate the number of ways to build an array of length 'n' with elements 
        ranging from 1 to 'm', such that the maximum value is found with a 
        search cost of 'k' times.
        
        Parameters:
        - n (int): Length of the array.
        - m (int): Maximum value an element in the array can take.
        - k (int): Desired search cost to find the maximum value.
        
        Returns:
        - int: The number of ways to construct the array with the given conditions. 
               The result is given modulo 10^9 + 7.
        """
        @cache
        def dp(i, max_so_far, remain):
            """
            Recursive helper function to calculate the number of ways to construct the rest 
            of the array from index 'i' such that the remaining search cost to achieve is 'remain', 
            and the maximum number encountered so far is 'max_so_far'.
            
            Parameters:
            - i (int): The current index in the array.
            - max_so_far (int): The maximum value encountered in the array until index 'i'.
            - remain (int): The remaining search cost required.
            
            Returns:
            - int: The number of ways to construct the rest of the array satisfying the conditions.
            
            """
            if i == n:
                if remain == 0:
                    return 1
                
                return 0
            
            # when ith number is lteq max_so_far
            # search cost doesn't increase when ith number is lteq max_so_far
            # max_so_far number of choices
            ans = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD

            # when ith number is gt max_so_far
            # search cost increases with ith values gt max_so_far 
            for num in range(max_so_far + 1, m + 1):
                ans = (ans + dp(i + 1, num, remain - 1)) % MOD
                
            return ans
        
        MOD = 10 ** 9 + 7
        return dp(0, 0, k)