class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        '''
        n stores
        m prod types
        quantities[i] -> qty of prod type i

        goal: all quantities should be distributed to all stores, minimizing max no. of prod 'x' given to any store.

        intuition:
            binary search, try all x from 1 to max(product), for each iteration, iterate over quantities, take count of how many stores can it serve. success is when the total count of stores it can serve should be >= n. then minimize 'x'
        '''

        def check(x):
            store_count = 0
            for q in quantities:
                store_count += ceil(q/x)
            return store_count <= n # able to distribute all products to the store (we are not checking if all stores got product)


        l, r = 1, max(quantities)
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1

        return l