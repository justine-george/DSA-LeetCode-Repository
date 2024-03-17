class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count, s2_count = [0] * 26, [0] * 26

        # first len(s1) characters of s1 and s2, fill the dict
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            added_index = ord(s2[r]) - ord('a')
            s2_count[added_index] += 1
            # now equal
            if s1_count[added_index] == s2_count[added_index]: matches += 1
            # were equal
            elif s1_count[added_index] + 1 == s2_count[added_index]: matches -= 1

            removed_index = ord(s2[l]) - ord('a')
            s2_count[removed_index] -= 1
            # now equal
            if s1_count[removed_index] == s2_count[removed_index]: matches += 1
            # were equal
            elif s1_count[removed_index] - 1 == s2_count[removed_index]: matches -= 1
            l += 1
        
        return matches == 26