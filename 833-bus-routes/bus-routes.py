class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        stop_to_routes = defaultdict(set)
        for r, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(r)

        visited_routes = set()
        visited_stops = set([source])
        q = deque([(source, 0)])  # (stop, buses_taken)

        while q:
            stop, buses = q.popleft()
            if stop == target:
                return buses
            for route in stop_to_routes[stop]:
                if route in visited_routes: 
                    continue
                visited_routes.add(route)
                for nxt in routes[route]:
                    if nxt not in visited_stops:
                        visited_stops.add(nxt)
                        q.append((nxt, buses + 1))
        return -1