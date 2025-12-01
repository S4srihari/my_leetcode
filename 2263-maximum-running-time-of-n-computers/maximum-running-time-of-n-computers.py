class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        arr = sorted(batteries)
        total = sum(batteries)
        while arr[-1] > total//n:
            total -= arr.pop()
            n -= 1 
        return total//n