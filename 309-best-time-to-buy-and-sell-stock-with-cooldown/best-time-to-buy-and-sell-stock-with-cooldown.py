class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[None]*(n+1) for _ in range(2)]

        def mp(can_buy,cur):
            if cur >= n:
                return 0

            if cache[can_buy][cur] is not None:
                return cache[can_buy][cur]
            elif can_buy == 1:
                buy = mp(0,cur+1)-prices[cur]
                not_buy = mp(1,cur+1)
                cache[can_buy][cur] = max(buy,not_buy)
                return cache[can_buy][cur]
            else :
                sell = mp(1,cur+2)+prices[cur]
                not_sell = mp(0,cur+1)
                cache[can_buy][cur] = max(sell,not_sell)
                return cache[can_buy][cur]
        mp(1,0)
        return cache[1][0]