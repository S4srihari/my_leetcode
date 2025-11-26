class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        mod = 10**9 + 7
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        v = grid[0][0]%k
        dp[0][0][v] = 1
        for i in range(m):
            for j in range(n):
                g = grid[i][j]%k
                for v in range(k):
                    dif = (v-g)%k
                    dp[i][j][v] = (dp[i][j][v] + dp[i-1][j][dif])%mod if i > 0 else dp[i][j][v]
                    dp[i][j][v] = (dp[i][j][v] + dp[i][j-1][dif])%mod if j>0 else dp[i][j][v]   
        return dp[m-1][n-1][0]