class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j == 0:
                    dp[i][j] = grid[i][j]
                else :
                    if i > 0:
                        up = grid[i][j] + dp[i-1][j]
                    else :
                        up = float('inf')
                    if j > 0:
                        left = grid[i][j] + dp[i][j-1]
                    else :
                        left = float('inf')
                    dp[i][j] = min(up,left)
        return dp[m-1][n-1]