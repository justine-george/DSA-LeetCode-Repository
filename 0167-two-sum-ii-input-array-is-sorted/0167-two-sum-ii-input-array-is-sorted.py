class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(t, i):
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                m = (l + r) // 2

                if numbers[m] == t and m != i:
                    return m
                
                if numbers[m] < t:
                    l = m + 1
                else:
                    r = m - 1
            return None


        for i, n in enumerate(numbers):
            val = bin_search(target - n, i)
            if val:
                return [i + 1, val + 1] if i < val else [val + 1, i + 1]