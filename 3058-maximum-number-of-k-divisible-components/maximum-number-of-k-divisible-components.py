class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        comps = 1
        def dfs(node,parent):
            nonlocal comps
            cur = values[node]
            for adj_node in adj_list[node]:
                if adj_node != parent:
                    val = dfs(adj_node, node)
                    if val%k == 0:
                        comps += 1
                    cur += val
            return cur
        dfs(0,-1)
        return comps