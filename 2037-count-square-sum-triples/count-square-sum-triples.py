class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for i in range(1,n):
            cur = i**2
            for j in range(1, n):
                val = (cur + j**2)**0.5
                if val  <= n and val%1 == 0:
                    cnt += 1
        return cnt