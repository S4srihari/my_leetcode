class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for start, end, weight in times:
            adj_list[start].append((end, weight))
        
        reach_times = [float("inf")] * (n+1)
        reach_times[k] = 0
        heap = [(0, k)] 
        
        while heap:
            cur_time, node = heapq.heappop(heap)
            for adj_node, weight in adj_list[node]:
                if cur_time + weight < reach_times[adj_node]:
                    reach_times[adj_node] = cur_time + weight 
                    heapq.heappush(heap, (reach_times[adj_node], adj_node))
        
        res = max(reach_times[1:])
        if res == float("inf"): return -1 
        return res