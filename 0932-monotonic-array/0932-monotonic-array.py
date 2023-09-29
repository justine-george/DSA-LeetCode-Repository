class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr_stack = []
        decr_stack = []

        incr, decr = True, True

        for n in nums:
            if incr or decr:
                # monotonic increasing
                if incr:
                    while incr_stack and incr_stack[-1] > n:
                        incr = False
                        break                
                    incr_stack.append(n)

                # monotonic decreasing
                if decr:
                    while decr_stack and decr_stack[-1] < n:
                        decr = False
                        break
                    decr_stack.append(n)
        
        return incr or decr