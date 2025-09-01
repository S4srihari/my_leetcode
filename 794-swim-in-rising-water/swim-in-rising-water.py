class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0],0,0)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            wt,i,j = heapq.heappop(heap)
            if visited[i][j]: continue
            if i == n-1 and j == n-1: 
                return wt
            visited[i][j] = True
            for di,dj in dirs:
                if 0<= i+di < n and 0 <= j+dj < n and not visited[i+di][j+dj]:
                    heapq.heappush(heap,(max(wt,grid[i+di][j+dj]),i+di,j+dj))
        return -1