class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_elem = max(arr1)
        count = [0] * (max_elem + 1)

        for n in arr1:
            count[n] += 1
        
        res = []
        # fill arr2 elements
        for n in arr2:
            while count[n] > 0:
                res.append(n)
                count[n] -= 1
        
        # fill remaining from arr1 not in arr2
        for n in range(max_elem + 1):
            while count[n] > 0:
                res.append(n)
                count[n] -= 1

        return res