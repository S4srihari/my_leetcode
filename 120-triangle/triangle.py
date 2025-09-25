class Solution:
    def f(self, i,j):
        if i == self.n : return 0
        if self.cache[i][j] != -1: return self.cache[i][j]
        frst = self.f(i+1,j) 
        sec = self.f(i+1,j+1) 
        self.cache[i][j] = min(frst, sec) + self.triangle[i][j]
        return self.cache[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cache = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(i,-1,-1):
                cache[i][j] = min(cache[i+1][j],cache[i+1][j+1]) + triangle[i][j]
        return cache[0][0]