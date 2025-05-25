class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(candi,cur,target):
            if target == 0:
                ans.append(cur[:])
                return
            for idx in range(len(candi)):
                if candi[idx] <= target:
                    cur.append(candi[idx])
                    backtrack(candi[idx:],cur,target-candi[idx])
                    cur.pop()
            return
        
        backtrack(candidates,[],target)
        return ans