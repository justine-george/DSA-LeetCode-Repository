class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # 2 = 5 ^ x
        # => x = 2 ^ 5

        # a^0 = a

        n = len(pref)
        arr = [0] * n

        arr[0] = pref[0]
        for i in range(1, n):
            arr[i] = pref[i - 1] ^ pref[i]
        
        return arr