class Solution:
    def check(self, left, right, strs):
        res = True
        for i in range(len(strs)):
            if strs[i][right] < strs[i][left]:
                res = False
                break
        return res

    def solve(self,idx, strs, prev, dp):
        if idx == len(strs[0]):
            return 0
        if (idx,prev) in dp:
            return dp[(idx,prev)]
        not_take = self.solve(idx+1, strs, prev, dp)
        take = 0
        if prev == -1 or self.check(prev, idx, strs) :
            take = self.solve(idx+1, strs, idx, dp) + 1
          
        dp[(idx, prev)] = max(take, not_take)
        return dp[(idx, prev)]
        
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = {}
        return len(strs[0]) - self.solve(0, strs, -1, dp)