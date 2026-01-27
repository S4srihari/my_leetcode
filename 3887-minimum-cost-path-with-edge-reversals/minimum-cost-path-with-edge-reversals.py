class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return -1
        reach_costs = [float("inf")]*n
        reach_costs[0] = 0
        adj_list = defaultdict(list)
        for st,end,weight in edges:
            adj_list[st].append((weight,end))
            adj_list[end].append((weight*2,st))

        heap = [(0,0)]
        while heap:
            cur_cost, cur_node = heapq.heappop(heap)
            if cur_node == n-1:
                return cur_cost
            for cost, adj_node in adj_list[cur_node]:
                if cur_cost + cost < reach_costs[adj_node]:
                    reach_costs[adj_node] = cur_cost + cost
                    heapq.heappush(heap, (cur_cost + cost, adj_node))
        return -1