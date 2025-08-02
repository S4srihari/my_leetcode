class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        prev  = [[0]*2 for _ in range(k+1)]
        cur = [[0]*2 for _ in range(k+1)]
        
        for idx in range(n-1,-1,-1):
            for lim in range(1,k+1):
                for can_buy in range(2):
                    if can_buy :
                        cur[lim][can_buy] = max(prev[lim][0] - prices[idx], prev[lim][1])
                    else:
                        cur[lim][can_buy] = max(prev[lim-1][1]+prices[idx],prev[lim][0])
            prev,cur = cur,prev
        return prev[k][1]