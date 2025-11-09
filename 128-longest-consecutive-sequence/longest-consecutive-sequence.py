class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in store:
            if num-1 in store:
                continue
            k = 0
            while num+k in store:
                k += 1
            res = max(res,k)
        return res