class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(idx,cur):
            res.append(cur[:])
            for i in range(idx,n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                backtrack(i+1,cur)
                cur.pop()

        backtrack(0,[])
        return res