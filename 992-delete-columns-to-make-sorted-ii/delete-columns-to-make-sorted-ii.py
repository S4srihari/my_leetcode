class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        sorted_pairs = [False]*(n-1)
        
        for j in range(m):
            bad = False
            for i in range(n-1):
                if not sorted_pairs[i] and strs[i][j] > strs[i+1][j]:
                    bad = True
                    break
            if bad:
                res += 1
                continue
            
            for i in range(n-1):
                if not sorted_pairs[i] and strs[i][j] < strs[i+1][j]:
                    sorted_pairs[i] = True
            if all(sorted_pairs):
                break
        return res