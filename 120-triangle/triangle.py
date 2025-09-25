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
        ahead = [0]*(n+1)
        cur = [0]*(n+1)

        for i in range(n-1,-1,-1):
            for j in range(i,-1,-1):
                cur[j] = min(ahead[j],ahead[j+1]) + triangle[i][j]
            cur,ahead = ahead,cur
        return ahead[0]