class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(i,cur_sum,cur_lis):
            if cur_sum == target:
                res.append(cur_lis[:])
                return
            elif cur_sum > target or i >= n:
                return
            
            for idx in range(i,n):
                if idx > i and candidates[idx] == candidates[idx-1]:
                    continue
                if cur_sum + candidates[idx] > target:
                    break
                cur_lis.append(candidates[idx])
                dfs(idx+1,cur_sum + candidates[idx],cur_lis)
                cur_lis.pop()
            return
        
        dfs(0,0,[])
        return res