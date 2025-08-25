class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]  # (time, node)
        
        while heap:
            curTime, node = heapq.heappop(heap)
            if curTime > dist[node]:
                continue
            for nei, w in adj[node]:
                if dist[node] + w < dist[nei]:
                    dist[nei] = dist[node] + w
                    heapq.heappush(heap, (dist[nei], nei))
        
        res = max(dist[1:])
        if res == float("inf"): return -1 
        return res