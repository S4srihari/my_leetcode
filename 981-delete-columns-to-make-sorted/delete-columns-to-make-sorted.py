class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = [False]*m
        for j in range(m):
            for i in range(1,n):
                if strs[i][j] < strs[i-1][j]:
                    res[j] = True
                    break
        return sum(res)