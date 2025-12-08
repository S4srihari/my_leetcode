class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        squares = set()
        for i in range(1,n+1):
            squares.add(i**2)
        limit = int(((n**2)/2)**0.5)
        for i in range(1,limit+1):
            for j in range(i+1,n+1):
                if i**2 + j**2 in squares:
                    cnt += 2
        return cnt