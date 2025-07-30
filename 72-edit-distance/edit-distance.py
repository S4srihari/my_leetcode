class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        cache = {}
        
        def dfs(i,j):
            if j < 0:
                return i+1
            if i < 0:
                return j+1
            if (i,j) in cache: return cache[(i,j)]
            if word1[i] == word2[j]:
                cache[(i,j)] = dfs(i-1,j-1)
                return cache[(i,j)]
            else:
                cache[(i,j)] = 1 + min(dfs(i,j-1),dfs(i-1,j),dfs(i-1,j-1))
                return cache[(i,j)]
        
        return dfs(m-1,n-1)