class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count = {chr(ord('a') + i): 0 for i in range(26)}
        s2_count = {chr(ord('a') + i): 0 for i in range(26)}

        # first len(s1) characters of s1 and s2, fill the dict
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        
        matches = 0
        for key in s1_count.keys():
            matches += (1 if s1_count[key] == s2_count[key] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            s2_count[s2[r]] += 1
            # now equal
            if s1_count[s2[r]] == s2_count[s2[r]]: matches += 1
            # were equal
            elif s1_count[s2[r]] + 1 == s2_count[s2[r]]: matches -= 1

            s2_count[s2[l]] -= 1
            # now equal
            if s1_count[s2[l]] == s2_count[s2[l]]: matches += 1
            # were equal
            elif s1_count[s2[l]] - 1 == s2_count[s2[l]]: matches -= 1
            l += 1
        
        return matches == 26