class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))

            while q:
                cr,cc = q.popleft()
                if cc+ 1 < n and grid[cr][cc+1]=="1" and (cr,cc+1) not in visited:
                    q.append((cr,cc+1))
                    visited.add((cr,cc+1))
                if cc - 1 >= 0 and grid[cr][cc-1]=="1" and (cr,cc-1) not in visited:
                    q.append((cr,cc-1))
                    visited.add((cr,cc-1))
                if cr+1 < m and grid[cr+1][cc] == "1" and (cr+1,cc) not in visited:
                    q.append((cr+1,cc))
                    visited.add((cr+1,cc))
                if cr-1 >= 0 and grid[cr-1][cc] == "1" and (cr-1,cc) not in visited:
                    q.append((cr-1,cc))
                    visited.add((cr-1,cc))
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands += 1
                    bfs(i,j)
        return islands