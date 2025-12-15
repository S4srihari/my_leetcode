class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        left = 0
        n = len(prices)
        if n == 1:
            return 1
        res = 0
        for right in range(1,n):
            if prices[right-1] - prices[right] != 1:
                dist = right - left
                res += int(dist*(dist+1)/2)
                left = right
        dist = n-left
        res += int(dist*(dist+1)/2)
        return res