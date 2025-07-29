class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m+n:
            return False
        
        dp = [[None]*(n+1) for _ in range(m+1)]
        
        def helper(i,j):
            if i == m and j == n:
                dp[i][j] = True
                return True
            if dp[i][j] is not None: return dp[i][j]
            if i < m and s1[i] == s3[i+j]:
                if helper(i+1,j): 
                    dp[i][j] = True
                    return True
            if j < n and s2[j] == s3[i+j]:
                if helper(i,j+1): 
                    dp[i][j] = True
                    return True
            dp[i][j] = False
            return False
        
        return helper(0,0)