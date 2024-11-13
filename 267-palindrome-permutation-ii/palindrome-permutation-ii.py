class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        N = len(s)
        s_freq_count = Counter(s)

        # Check if a palindromic permutation is possible
        if sum(v % 2 for v in s_freq_count.values()) > 1:
            return []

        # Identify half characters for permutation
        half_chars = []
        middle_char = ""
        for k, v in s_freq_count.items():
            half_chars.extend([k] * (v // 2))
            if v % 2 == 1:
                middle_char = k

        # Generate all unique permutations of the half characters
        # unique_permutations = set(itertools.permutations(half_chars))
        unique_permutations = self.get_permutations(half_chars)
        # unique_permutations = self.get_unique_permutations(half_chars)

        # Construct palindromes from unique permutations
        ans = []
        for p in unique_permutations:
            half = ''.join(p)
            ans.append(half + middle_char + half[::-1])
            
        return ans
    
    def get_permutations(self, arr):
        if len(arr) == 0:
            return [[]]
        permutations = self.get_permutations(arr[1:])
        res = set()
        for p in permutations:
            for i in range(len(p) + 1):
                new_p = tuple(p[:i]) + tuple([arr[0]]) + tuple(p[i:])
                res.add(new_p)
        return res
    
    def get_unique_permutations(self, arr):
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