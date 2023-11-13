class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        vowels = [s[i] for i in range(n) if s[i] in vowel_set]
        vowels.sort(reverse = True)

        return "".join([vowels.pop() if s[i] in vowel_set else s[i] for i in range(n)])