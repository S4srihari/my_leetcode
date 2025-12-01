class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        res = 0
        left, right = 0, 2*10**14
        def possible(val):
            tot = 0
            for bat in batteries:
                tot += min(bat, val)
            return tot//n >= val
        while left <= right:
            mid = left + (right-left)//2
            if possible(mid):
                res = mid
                left = mid+1
            else:
                right = mid-1 
        return res