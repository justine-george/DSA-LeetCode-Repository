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
        unique_permutations = set(itertools.permutations(half_chars))

        # Construct palindromes from unique permutations
        ans = []
        for p in unique_permutations:
            half = ''.join(p)
            ans.append(half + middle_char + half[::-1])
            
        return ans