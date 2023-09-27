class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # T: O(n * m), since k has a limit of 20. If no limit, T: O(n * m * k)
        # S: O(n)
        # bottom up dp
        dp = [False] * (len(s) + 1) # extra 1 for the base case 

        # Trivial case: to match empty, take nothing from the dict! 
        # If we reach the end, we were able to match the word with the dict.
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            # go through each dict word, try to find match
            for word in wordDict:
                if s[i: i + len(word)] == word and dp[i + len(word)]:
                    # match found and the remaining part of s is found in the dict
                    dp[i] = True
                    break
        return dp[0]