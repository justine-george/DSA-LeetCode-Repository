class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        gap_counter = defaultdict(int)
        for i in range(len(stations) - 1):
            gap_counter[stations[i + 1] - stations[i]] += 1

        def check(delta):
            new_station_count = 0
            for gap, freq in gap_counter.items():
                # total number of new stations added
                new_station_count += freq * (ceil(gap / delta) - 1)
                if new_station_count > k:
                    return False
            return new_station_count <= k

        initialMaxDist = max([stations[i + 1] - stations[i] for i in range(len(stations) - 1)])
        l, r = 1e-6, initialMaxDist
        while r - l > 1e-6:
            m = l + (r - l) / 2
            if check(m):
                r = m
            else:
                l = m
        return l