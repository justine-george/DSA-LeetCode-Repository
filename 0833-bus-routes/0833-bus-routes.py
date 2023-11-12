class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # {stop: bus that stop here}
        adj = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                adj[stop].add(bus)
        if target not in adj:
            return -1
        
        queue = deque([(source, 0)])
        visited_buses = set()
        visited_stops = set()
        while queue:
            stop, route_len = queue.popleft()
            if stop == target:
                return route_len
            
            for bus in adj[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)

                    for stop in routes[bus]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop, route_len + 1))
        
        return -1


