class Solution:
    def minimumSteps(self, s: str) -> int:
        next_zero_pos = 0
        min_steps = 0
        # shift zeros to left
        for r in range(len(s)):
            if s[r] == '0':
                # count number of swaps to move to next_zero_pos
                min_steps += r - next_zero_pos
                next_zero_pos += 1

        return min_steps