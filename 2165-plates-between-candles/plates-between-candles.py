class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        def get_left_candle_boundary(start, candle_pos):
            # get left boundary
            # ie. find left such that start <= left

            l, r = 0, len(candle_pos) - 1
            while l <= r:
                m = (r + l) // 2
                if candle_pos[m] == start:
                    return m
                elif candle_pos[m] < start:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        def get_right_candle_boundary(end, candle_pos):
            # get right boundary
            # ie. find right such that right <= end

            l, r = 0, len(candle_pos) - 1
            while l <= r:
                m = (r + l) // 2
                if candle_pos[m] == end:
                    return m
                elif candle_pos[m] < end:
                    l = m + 1
                else:
                    r = m - 1
            return r

        # calculate prefix count of plates
        pre = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            pre[i] = pre[i - 1] + (1 if s[i - 1] == '*' else 0)

        # make a sorted list of candle positions to enable binary search
        candle_pos = [i for i, c in enumerate(s) if c == '|']

        res = []
        for start, end in queries:
            left_index = get_left_candle_boundary(start, candle_pos)
            right_index = get_right_candle_boundary(end, candle_pos)
            if left_index == -1 or right_index == -1 or left_index >= right_index:
                res.append(0)
            else:
                res.append(pre[candle_pos[right_index] + 1] - pre[candle_pos[left_index]])
        
        return res