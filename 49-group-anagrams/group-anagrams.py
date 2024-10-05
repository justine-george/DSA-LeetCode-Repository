class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            # key = ''.join(sorted(s))
            key = sorted(s)
            map[tuple(key)].append(s)
        return map.values()