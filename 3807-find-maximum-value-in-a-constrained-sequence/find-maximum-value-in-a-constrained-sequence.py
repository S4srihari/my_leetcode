class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        res = [float("inf")]*n
        res[0] = 0
        for idx, val in restrictions:
            res[idx] = min(res[idx], val)
        for i in range(1,n):
            res[i] = min(res[i], res[i-1]+diff[i-1])
        for i in range(n-2,0,-1):
            res[i] = min(res[i], res[i+1]+diff[i])
        return max(res)

        # Tc = O(n)
        # Sc = O(n)