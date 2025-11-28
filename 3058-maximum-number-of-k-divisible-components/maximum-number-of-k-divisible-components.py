class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        vis = set()
        comps = 1
        def dfs(node):
            nonlocal comps
            vis.add(node)
            cur = values[node]
            for adj_node in adj_list[node]:
                if adj_node not in vis:
                    val = dfs(adj_node)
                    if val%k == 0:
                        comps += 1
                    cur += val
            return cur
        dfs(0)
        return comps