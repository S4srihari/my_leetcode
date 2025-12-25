class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = [i*(-1) for i in happiness]
        heapq.heapify(happiness)
        res = 0
        for i in range(k):
            res += max(0, heapq.heappop(happiness)*(-1) - i)
        return res