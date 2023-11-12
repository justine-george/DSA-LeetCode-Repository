class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # build graph
        # {stop: set() buses that stop at this stop}
        graph = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
        
        if target not in graph:
            return -1

        visited_buses = set()
        visited_stops = set()
        # (stop, # of buses taken)
        queue = deque([(source, 0)])
        while queue:
            stop, route_len = queue.popleft()
            if stop == target:
                return route_len

            for bus in graph[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    
                    for stop in routes[bus]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop, route_len + 1))

        return -1