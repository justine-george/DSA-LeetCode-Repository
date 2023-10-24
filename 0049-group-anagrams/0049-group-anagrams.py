class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cMap = defaultdict(list)

        def getFreq(word):
            map = defaultdict(int)
            for c in sorted(word):
                map[c] += 1
            res = []
            for key in map:
                res.append(str(key) + str(map[key]))
            return "".join(res)

        for word in strs:
            freqMap = getFreq(word)
            print(freqMap)
            cMap[freqMap].append(word)
        
        return cMap.values()