class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0
        for num in nums:
            cur *= 2 
            cur += num
            res.append(cur%5 == 0)
        return res