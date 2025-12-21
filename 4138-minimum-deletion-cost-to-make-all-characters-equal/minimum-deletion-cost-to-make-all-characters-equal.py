class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total = {}
        for i in range(len(cost)):
            total[s[i]] = total.get(s[i],0) + cost[i]
        maxi = max(total.values())
        return sum(total.values()) - maxi