class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        adj = defaultdict(list)
        n = numCourses
        in_degree = [0]*n
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])
            in_degree[edge[0]] += 1 
        
        from collections import deque
        que = deque()
        for vert in range(n):
            if in_degree[vert] == 0:
                que.append(vert)
                
        topo_order = []        
        while que:
            vert = que.popleft()
            topo_order.append(vert)
            for adj_v in adj[vert]:
                in_degree[adj_v] -= 1
                if in_degree[adj_v] == 0:
                    que.append(adj_v)
        
        return topo_order if len(topo_order) == n else []