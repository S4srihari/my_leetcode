class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        cache = {}

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
        
        return dfs(0,0)
        
