class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        vowels = [s[i] for i in range(n) if s[i] in vowel_set]
        # vowels.sort(reverse = True)

        # return "".join([vowels.pop() if s[i] in vowel_set else s[i] for i in range(n)])
        vowel_indices = [i for i in range(n) if s[i] in vowel_set]
        vowels.sort()

        d = {i: v for i, v in zip(vowel_indices, vowels)}

        res = []
        for i in range(n):
            if s[i] in vowel_set:
                res.append(d[i])
            else:
                res.append(s[i])

        return "".join(res)