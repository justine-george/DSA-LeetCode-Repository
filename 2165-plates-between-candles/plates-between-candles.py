class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        plate_count = [0] * n
        left_candle_index = [0] * n
        right_candle_index = [0] * n

        plate_count[0] = 1 if s[0] == '*' else 0
        left_candle_index[0] = 0 if s[0] == '|' else -1
        for i in range(1, n):
            plate_count[i] = plate_count[i - 1] + (1 if s[i] == '*' else 0)
            left_candle_index[i] = i if s[i] == '|' else left_candle_index[i - 1]
        
        right_candle_index[n - 1] = n - 1 if s[i] == '|' else n
        for i in range(n - 2, -1, -1):
            right_candle_index[i] = i if s[i] == '|' else right_candle_index[i + 1]
        
        res = []
        for start, end in queries:
            left = right_candle_index[start]
            right = left_candle_index[end]

            res.append(0 if left >= right else plate_count[right] - plate_count[left])

        return res





