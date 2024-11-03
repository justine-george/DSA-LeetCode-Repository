class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            # key = ''.join(sorted(s))
            charmap = [0] * 26
            for c in s:
                charmap[ord(c) - ord('a')] += 1
            map[tuple(charmap)].append(s)

        return list(map.values())