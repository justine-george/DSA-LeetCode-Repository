class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))

        memo = {}
        def dfs(i):
            if i == len(intervals):
                return 0

            if i in memo:
                return memo[i]
            
            # dont include
            skip_current = dfs(i + 1)

            # include, find out next_index, ie. next possible index
            # next_index = i + 1
            # while next_index < len(intervals) and intervals[next_index][0] < intervals[i][1]:
            #     next_index += 1

            # better: use binary search to find next_index
            # smallest index x that satisfies x's start time >= cur's end time
            # ie. smallest x that satisfies intervals[x][0] >= intervals[i][1]
            l, r = i + 1, len(intervals)
            while l < r:
                mid = l + (r - l) // 2
                if intervals[mid][0] >= intervals[i][1]:
                    r = mid
                else:
                    l = mid + 1
            take_current = intervals[i][2] + dfs(l)
            
            memo[i] = max(take_current, skip_current)
            return memo[i]

        return dfs(0)