class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(rate,lis,hrs):
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile/rate)
            return cnt <= hrs

        m, n = max(piles), len(piles)
        ans = m
        left,right = 1,m
        while left <= right:
            mid = left + (right -left)//2
            if can_eat(mid,piles,h):
                ans = mid
                right = mid -1
            else :
                left = mid + 1
        return ans