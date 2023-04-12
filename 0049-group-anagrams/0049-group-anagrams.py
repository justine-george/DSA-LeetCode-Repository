class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(m*n)
        res = collections.defaultdict(list) # mapping charcount list of words that are anagrams
        
        for word in strs:
            count = [0] * 26 # one for each character a- z
            for c in word:
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(word)
                
        return res.values()