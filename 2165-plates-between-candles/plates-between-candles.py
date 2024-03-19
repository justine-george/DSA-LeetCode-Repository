class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # n = len(s)
        # plate_count = [0] * n
        # left_candle_index = [0] * n
        # right_candle_index = [0] * n

        # plate_count[0] = 1 if s[0] == '*' else 0
        # left_candle_index[0] = 0 if s[0] == '|' else -1
        # for i in range(1, n):
        #     plate_count[i] = plate_count[i - 1] + (1 if s[i] == '*' else 0)
        #     left_candle_index[i] = i if s[i] == '|' else left_candle_index[i - 1]
        
        # right_candle_index[n - 1] = n - 1 if s[i] == '|' else n
        # for i in range(n - 2, -1, -1):
        #     right_candle_index[i] = i if s[i] == '|' else right_candle_index[i + 1]
        
        # res = []
        # for start, end in queries:
        #     left = right_candle_index[start]
        #     right = left_candle_index[end]

        #     res.append(0 if left >= right else plate_count[right] - plate_count[left])

        # return res


        def get_first_candle_index_right_of(start, candle_pos):
            # ie. find left such that start <= left

            # template: minimize k such that condition(k) is True

            l, r = 0, len(candle_pos) - 1
            while l < r:
                m = (r + l) // 2
                if candle_pos[m] >= start:
                    r = m
                else:
                    l = m + 1
            return l
        
        def get_first_candle_index_left_of(end, candle_pos):
            # ie. find right such that right <= end

            # template: maximize k such that condition(k) is True

            l, r = 0, len(candle_pos) - 1
            while l <= r:
                m = (l + r) // 2
                if candle_pos[m] <= end:
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
            candle_index_start = \
                get_first_candle_index_right_of(start, candle_pos)
            candle_index_end = \
                get_first_candle_index_left_of(end, candle_pos)
                
            if candle_index_start == -1 or \
                candle_index_end == -1 or \
                candle_index_start >= candle_index_end:
                res.append(0)
            else:
                res.append(pre[candle_pos[candle_index_end] + 1] - pre[candle_pos[candle_index_start]])
        
        return res