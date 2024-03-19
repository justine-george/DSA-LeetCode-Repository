class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left_candle = [-1] * len(s)
        right_candle = [-1] * len(s)

        for i in range(1, len(s)):
            left_candle[i] = i if s[i] == '|' else left_candle[i - 1]
        
        for i in range(len(s) - 2, -1, -1):
            right_candle[i] = i if s[i] == '|' else right_candle[i + 1]

        print(left_candle)
        print(right_candle)
        
        # running sum of plates
        plate_count = [0] * len(s)
        plate_count[0] = 1 if s[0] == '*' else 0
        for i in range(1, len(s)):
            plate_count[i] = plate_count[i - 1] + (1 if s[i] == '*' else 0)

        res = []
        for start, end in queries:
            left = right_candle[start]
            right = left_candle[end]

            if left == -1 or right == -1:
                res.append(0)
            else:
                count = plate_count[right] - plate_count[left]
                res.append(count if count > 0 else 0)

        return res





