class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cMap = defaultdict(list)

        def getFreq(word):
            charmap = [0] * 26
            for c in word:
                charmap[ord(c) - ord('a')] += 1
            res = ""
            for i in charmap:
                res += "#" + str(i)
            return res

        for word in strs:
            freqMap = getFreq(word)
            cMap[freqMap].append(word)
        
        return cMap.values()