class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            odds = set()
            evens = set()
            for j in range(i,len(nums)):
                if nums[j]%2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])
                
                if len(odds) == len(evens):
                    res = max(res, j-i+1)

        return res