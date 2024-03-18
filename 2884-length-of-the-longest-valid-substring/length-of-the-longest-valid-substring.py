class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        max_len = 0
        invalid_set = set(forbidden)

        l = r = len(word) - 1
        while l >= 0:
            # update r if needed
            for j in range(l, min(r, l + 9) + 1):
                if word[l: j + 1] in invalid_set:
                    r = j - 1
                    break

            # update max_len
            max_len = max(max_len, r - l + 1)
            l -= 1

        return max_len