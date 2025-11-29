class Solution:
    def possible(self, val, points, m):
        n, tot = len(points), 0
        moves = n
        cur = 1
        for i in range(n-1):
            req = (val + points[i] -1)//points[i]
            if cur < req:
                needed = req-cur
                moves += needed * 2 
                cur = needed + 1
            else :
                cur = 1
            if moves > m+1:
                return False
        
        req = (val + points[-1] -1)//points[-1]
        if cur < req :
            moves += (req-cur)*2
        elif req < cur :
            moves -= 1
        return moves <= m

    def maxScore(self, points: List[int], m: int) -> int:
        res = 0
        left, right = 0, pow(10,16)
        while left <= right:
            mid = left + (right-left)//2
            if self.possible(mid, points, m):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res