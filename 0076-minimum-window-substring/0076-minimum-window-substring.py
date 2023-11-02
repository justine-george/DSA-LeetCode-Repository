class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tMap = Counter(t)
        windowMap = defaultdict(int)
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(tMap)

        l = 0
        for r in range(len(s)):
            c = s[r]
            windowMap[c] += 1

            if c in tMap and windowMap[c] == tMap[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                lChar = s[l]
                windowMap[lChar] -= 1
                if lChar in tMap and windowMap[lChar] < tMap[lChar]:
                    have -= 1

                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""