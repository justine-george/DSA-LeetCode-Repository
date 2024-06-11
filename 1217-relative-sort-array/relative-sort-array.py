class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        elems = set(arr2)
        start_arr = [n for n in arr1 if n in elems]
        count_map = Counter(start_arr)

        res = []
        for n in arr2:
            for i in range(count_map[n]):
                res.append(n)

        end_arr = sorted([n for n in arr1 if n not in elems])
        return res + end_arr