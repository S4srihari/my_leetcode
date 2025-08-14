class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur_sum,cur_lis):
            if cur_sum == target:
                res.append(cur_lis[:])
                return
            elif cur_sum > target or i >= len(candidates):
                return
            else:
                cur_lis.append(candidates[i])
                dfs(i,cur_sum + candidates[i],cur_lis)
                cur_lis.pop()
                dfs(i+1,cur_sum,cur_lis)
                return
        
        dfs(0,0,[])
        return res