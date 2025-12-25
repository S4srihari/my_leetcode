class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        for i in range(k):
            res += max(0,happiness.pop() - i)
        return res