class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = [False]*m
        cur = [i for i in strs[0]]
        for i in range(1,n):
            for j in range(m):
                if strs[i][j] < cur[j]:
                    res[j] = True
                cur[j] = strs[i][j]
        return sum(res)