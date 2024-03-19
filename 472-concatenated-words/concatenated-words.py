class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)

        dp = {}
        def dfs(word):
            if word in dp:
                return dp[word]

            # go through all prefixes of this word
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if (prefix in word_set and suffix in word_set) or (prefix in word_set and dfs(suffix)):
                    dp[word] = True
                    return True

            dp[word] = False
            return False

        res = []

        for w in words:
            if dfs(w):
                res.append(w)

        return res