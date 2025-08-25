class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges: return None
        parent = [i for i in range(len(edges)+1)]

        def union(u,v):
            parent[find(u)] = find(v)
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        visited = set()
        for u,v in edges:
            if u in visited and v in visited and find(u) == find(v):
                return [u,v]
            else:
                visited.add(u)
                visited.add(v)
                union(u,v)
        
        return None