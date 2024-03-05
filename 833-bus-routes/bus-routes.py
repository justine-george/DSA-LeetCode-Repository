class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # targetPresent = False
        # for route in routes:
        #     if target in route:
        #         targetPresent = True
        # if not targetPresent:
        #     return False
        
        graph = collections.defaultdict(set)
        queue = collections.deque([(source, 0)])

        for bus, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(bus)
        
        visited_stops = set()
        visited_buses = set()
        
        while queue:
            stop, no_of_buses = queue.popleft()

            if stop == target:
                return no_of_buses

            for bus in graph[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for busstop in routes[bus]:
                        if busstop not in visited_stops:
                            visited_stops.add(busstop)
                            queue.append((busstop, no_of_buses + 1))

        return -1