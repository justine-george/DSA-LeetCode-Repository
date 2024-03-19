class Solution:
    def minimumKeypresses(self, s: str) -> int:
        char_count = Counter(s)

        res = 0
        multiplier = 0

        for i, freq in enumerate(sorted(char_count.values(), reverse=True)):
            # 0 -> 8   = 1 is the multiplier
            # 9 -> 17  = 2 is the multiplier
            # 18 -> 25 = 3 is the multiplier

            # time to change multiplier
            if i % 9 == 0:
                multiplier += 1

            res += (freq * multiplier)

        return res

        # return sum((i // 9 + 1) * freq for i, freq in enumerate(sorted(Counter(s).values(), reverse=True)))