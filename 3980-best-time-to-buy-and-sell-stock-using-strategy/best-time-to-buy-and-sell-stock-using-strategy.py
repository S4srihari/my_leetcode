class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        res = float("-inf")
        cur = 0
        n = len(prices)
        for i in range(n):
            cur += prices[i]*strategy[i]
        res = max(res,cur)
        for i in range(k):
            if i < k//2:
                cur -= prices[i]*strategy[i]
            else:
                if strategy[i] == 0:
                    cur += prices[i]
                elif strategy[i] == -1:
                    cur += prices[i]*2
        res = max(res,cur)
        for i in range(k, n):
            cur += prices[i-k]*strategy[i-k]
            if strategy[i] == 0:
                cur += prices[i]
            elif strategy[i] == -1:
                cur += prices[i]*2
            cur -= prices[i-(k//2)]
            res = max(res,cur)
        return res

