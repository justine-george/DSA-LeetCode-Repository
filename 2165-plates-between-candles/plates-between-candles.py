class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Helper function to find the index of the leftmost candle to the right of a given position
        def get_left_candle_boundary(start, candle_pos):
            l, r = 0, len(candle_pos) - 1
            while l <= r:
                m = (l + r) // 2
                if candle_pos[m] < start:
                    l = m + 1
                else:
                    r = m - 1
            return l if l < len(candle_pos) else -1

        # Helper function to find the index of the rightmost candle to the left of a given position
        def get_right_candle_boundary(end, candle_pos):
            l, r = 0, len(candle_pos) - 1
            while l <= r:
                m = (l + r) // 2
                if candle_pos[m] <= end:
                    l = m + 1
                else:
                    r = m - 1
            return r if r >= 0 else -1

        # Calculate prefix count of plates
        pre = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            pre[i] = pre[i - 1] + (1 if s[i - 1] == '*' else 0)

        # Make a list of candle positions
        candle_pos = [i for i, c in enumerate(s) if c == '|']

        res = []
        for start, end in queries:
            left_index = get_left_candle_boundary(start, candle_pos)
            right_index = get_right_candle_boundary(end, candle_pos)
            if left_index == -1 or right_index == -1 or left_index >= right_index:
                res.append(0)
            else:
                # Calculate the number of plates between the leftmost and rightmost candles in the query range
                res.append(pre[candle_pos[right_index] + 1] - pre[candle_pos[left_index]])
        return res