class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cMap = defaultdict(list)
        for word in strs:
            charmap = [0] * 26
            for c in word:
                charmap[ord(c) - ord('a')] += 1
            cMap[tuple(charmap)].append(word)
        return cMap.values()