class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        N = len(s)
        s_freq_count = Counter(s)
            
        def get_unique_permutations(arr):
            arr_freq_count = Counter(arr)
            perm = []
            res = []
            def perm_helper():
                if len(perm) == len(arr):
                    res.append(perm[:])
                    return
                for k in arr_freq_count:
                    if arr_freq_count[k] > 0:
                        arr_freq_count[k] -= 1
                        perm.append(k)
                        perm_helper()
                        perm.pop()
                        arr_freq_count[k] += 1
            perm_helper()
            return res

        if N % 2 == 0:
            # shouldn't be possible when s length is even
            if any(v % 2 == 1 for v in s_freq_count.values()):
                return []
            
            good = []
            # half the size for easier computation of permutations
            for k, v in s_freq_count.items():
                good.extend([k] * (v // 2))

            ans = []
            for p in get_unique_permutations(good):
                r = "".join(p)
                r += r[::-1]
                ans.append(r)
            return ans
        else:
            if len([v for v in s_freq_count.values() if v % 2 == 1]) != 1:
                return []

            good = []
            # half the size for easier computation of permutations
            for k, v in s_freq_count.items():
                good.extend([k] * (v // 2))
            
            middle = next(k for k, v in s_freq_count.items() if v % 2 == 1)

            ans = []
            for p in get_unique_permutations(good):
                r = "".join(p)
                r += middle + r[::-1]
                ans.append(r)
            return ans