class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        maxArea = 0
        vis = [[False]*n for _ in range(m)]

        def dfs(i,j):
            area = 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for di,dj in directions:
                if 0<= i+di < m and 0<= j +dj < n and not vis[i+di][j+dj] and grid[i+di][j+dj] == 1:
                    vis[i+di][j+dj] = True
                    area += dfs(i+di,j+dj)
            return area


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    vis[i][j] = True
                    maxArea = max(maxArea,dfs(i,j))
        return maxArea