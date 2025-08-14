class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i,cur):
            if i >= len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            backtrack(i+1,cur)
            cur.pop()
            backtrack(i+1,cur)
            return
        
        backtrack(0,[])
        return res