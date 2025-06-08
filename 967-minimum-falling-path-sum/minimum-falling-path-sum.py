class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [float('inf')] + matrix[0] + [float('inf')] 
        for r in range(1,n):
            temp = [0]*n
            for j in range(n):
                temp[j] = matrix[r][j] + min(dp[j+1],dp[j],dp[j+2])
            dp = [float('inf')] + temp + [float('inf')]
        return min(dp)