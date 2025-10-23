class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """def dfs(node, parent, depth, children, color):
            res = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, depth + 1, children, color)
            return res

        def build(n, edges, color):
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = dfs(0, -1, 0, children, color)
            return [res, n - res]"""


        def bfs(l, adjList, vis):
            res = [0]*l
            que = deque([(0,"red")])
            reds, blues = 0,0
            while que:
                node, color = que.pop()
                if node in vis: continue
                vis.add(node)
                if color == "red": reds += 1
                else : blues += 1
                res[node] = color
                for adjNode in adjList[node]:
                    if adjNode not in vis:
                        if color == "red": que.append((adjNode, "blue"))
                        else: que.append((adjNode, "red"))
            for i in range(l):
                if res[i] == "red": res[i] = reds
                else: res[i] = blues
            
            return res


        n = len(edges1) + 1
        m = len(edges2) + 1
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        counts1 = bfs(n, adj1, set())
        counts2 = bfs(m, adj2, set())
        res = [0] * n
        maxi = max(counts2)
        for i in range(n):
            res[i] = counts1[i] + maxi 
        return res