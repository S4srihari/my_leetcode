class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        n = len(target)
        for i in range(1,n):
            if target[i] < target[i-1]:
                res += target[i-1] - target[i]
        return res + target[-1] 