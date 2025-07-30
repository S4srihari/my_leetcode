class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        dp = [[-1]*(n) for _ in range(m)]
        def dfs(i,j,prev):
            if i<0 or j<0 or i >= m or j >= n or prev >= matrix[i][j]:
                return 0
            cur = 1
            if dp[i][j] != -1: return dp[i][j]
            for dx,dy in directions:
                cur = max(cur,1 + dfs(i+dx,j+dy,matrix[i][j]))
            dp[i][j] = cur
            return cur
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res,dfs(i,j,float("-inf")))
        return res