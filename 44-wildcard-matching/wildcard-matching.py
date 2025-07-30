class Solution:
    def dfs(i,j):
            if i == m and j == n:
                return True
            if j == n:
                return False
            if i == m:
                while j < n:
                    if p[j] != "*":
                        return False
                    else :
                        j += 1
                return True
            if (i,j) in cache: return cache[(i,j)]
            if s[i] == p[j] or p[j] == '?':
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]
            elif p[j] == "*":
                cache[(i,j)] =  dfs(i,j+1) or dfs(i+1,j)
                return cache[(i,j)]
            else:
                cache[(i,j)] = False
                return cache[(i,j)]

    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[m][n] = True
        for j in range(n-1,-1,-1):
            if p[j] == "*":
                dp[m][j] = dp[m][j+1]
            else :
                dp[m][j] = False

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i+1][j+1]
                elif p[j] == "*":
                    dp[i][j] =  dp[i][j+1] or dp[i+1][j]
                else:
                    dp[i][j] = False
        return dp[0][0]